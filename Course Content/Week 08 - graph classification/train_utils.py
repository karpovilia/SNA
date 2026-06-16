import matplotlib.pyplot as plt
import numpy as np
import torch as th
import torch.nn.functional as F
from ogb.graphproppred import Evaluator
from scipy import stats


class Logger(object):
    def __init__(self, runs, info=None):
        self.info = info
        self.results = [[] for _ in range(runs)]

    def add_result(self, run, result):
        assert len(result) == 3
        assert run >= 0 and run < len(self.results)
        self.results[run].append(result)

    def print_statistics(self, run=None):
        if run is not None:
            result = 100 * th.tensor(self.results[run])
            argmax = result[:, 1].argmax().item()
            print(f"Run {run + 1:02d}:")
            print(f"Highest Train: {result[:, 0].max():.2f}")
            print(f"Highest Valid: {result[:, 1].max():.2f}")
            print(f"  Final Train: {result[argmax, 0]:.2f}")
            print(f"   Final Test: {result[argmax, 2]:.2f}")
        else:
            result = 100 * th.tensor(self.results)

            best_results = []
            for r in result:
                train1 = r[:, 0].max().item()
                valid = r[:, 1].max().item()
                train2 = r[r[:, 1].argmax(), 0].item()
                test = r[r[:, 1].argmax(), 2].item()
                best_results.append((train1, valid, train2, test))

            best_result = th.tensor(best_results)

            print(f"All runs:")
            r = best_result[:, 0]
            print(f"Highest Train: {r.mean():.2f} ± {r.std():.2f}")
            r = best_result[:, 1]
            print(f"Highest Valid: {r.mean():.2f} ± {r.std():.2f}")
            r = best_result[:, 2]
            print(f"  Final Train: {r.mean():.2f} ± {r.std():.2f}")
            r = best_result[:, 3]
            print(f"   Final Test: {r.mean():.2f} ± {r.std():.2f}")


def train_epoch(model, dataloader, optimizer, device):

    model = model.train()
    model = model.to(device)

    logging = dict()

    total_loss = total_examples = 0
    for batched_graph, labels in dataloader:


        optimizer.zero_grad()
        pred = model(batched_graph.to(device))

        loss = F.binary_cross_entropy_with_logits(pred, labels.float().to(device))
        loss.backward()
        optimizer.step()

        logging.update(
            dict(
                bs=pred.shape[0],
                loss=loss.item(),
            )
        )

        # print(logging)
        num_examples = pred.shape[0]
        total_loss += loss.item() * num_examples
        total_examples += num_examples

    return total_loss / total_examples


@th.no_grad()
def test(model, loader, device):
    model = model.to(device)
    model.eval()
    evaluator = Evaluator(name="ogbg-molhiv")

    y_true = []
    y_pred = []

    for batched_graph, labels in loader:
        batched_graph = batched_graph.to(device)

        pred = model(batched_graph)
        y_true.append(labels.view(pred.shape).detach().cpu())
        y_pred.append(pred.detach().cpu())

    y_true = th.cat(y_true, dim=0).numpy()
    y_pred = th.cat(y_pred, dim=0).numpy()

    input_dict = {"y_true": y_true, "y_pred": y_pred}

    return evaluator.eval(input_dict)['rocauc']

def train(model, dl_train, dl_val, dl_test, device, logger, args, run):
    """
    A complete model training loop
    """
    optimizer = th.optim.Adam(
        model.parameters(),
        lr=args["lr"],
    )

    for epoch in range(1, 1 + args["epochs"]):
        loss = train_epoch(
            model,
            dl_train,
            optimizer,
            device,
        )

        if epoch % args["eval_steps"] == 0:
            train_roc = test(model, dl_train, device)
            val_roc = test(model, dl_val, device)
            test_roc = test(model, dl_test, device)
            result = [train_roc, val_roc, test_roc]
            logger.add_result(run, result)

            if epoch % args["log_steps"] == 0:
                print(
                    f"Run: {run+1:02d}, "
                    f"Epoch: {epoch:02d}, "
                    f"Loss: {loss:.4f}, "
                    f"Train: {train_roc:.4f} AUC, "
                    f"Valid: {val_roc:.4f} AUC, "
                    f"Test: {test_roc:.4f} AUC"
                )
                print("---")

    return logger


def repeat_experiments(
    model, dl_train, dl_val, dl_test, device, train_args, n_runs
):
    logger = Logger(n_runs, train_args)

    for run in range(n_runs):
        model.reset_parameters()

        logger = train(
            model,
            dl_train,
            dl_val,
            dl_test,
            device,
            logger,
            train_args,
            run,
        )

        logger.print_statistics(run)

    logger.print_statistics()
    return logger
