[video](https://youtu.be/yt47x4O5Vao) 
![[whiteboard.png]]

- Competition among memes in a world with limited attention, [nature](https://www.nature.com/articles/srep00335), 2012
- Inf2vec: Latent Representation Model for Social Influence Embedding, [IEEE](https://ieeexplore.ieee.org/document/8509310), 2018
- Inf-VAE: A Variational Autoencoder Framework to Integrate Homophily and Influence in Diffusion Prediction, [WSDM](https://arxiv.org/abs/2001.00132), 2020

https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology


## The SIR model [wiki](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)

The **SIR model** is one of the simplest compartmental models, and many models are derivatives of this basic form. The model consists of three compartments:

- **S**: The number of **s**usceptible individuals. When a susceptible and an infectious individual come into "infectious contact", the susceptible individual contracts the disease and transitions to the infectious compartment.
- **I**: The number of **i**nfectious individuals. These are individuals who have been infected and are capable of infecting susceptible individuals.
- **R** for the number of **r**emoved (and immune) or deceased individuals. These are individuals who have been infected and have either recovered from the disease and entered the removed compartment, or died. It is assumed that the number of deaths is negligible with respect to the total population. This compartment may also be called "**r**ecovered" or "**r**esistant".


SIR model takes population, infected cases, recovered cases as input. The model is able to give predictions for an arbitrary time period. As an output, it gives the number of infected and recovery cases.

**Model description** The SIR model is one of the simplest compartmental models, and many models are derivatives of this basic form. The model consists of three compartments: S for the number of susceptible, I for the number of infectious, and R for the number of recovered or deceased (or immune) individuals. SIR system can be described by the following set of ODE:
$$\frac{ds}{dt}= -\frac{βIS}{N}$$
$$\frac{dI}{dt}= \frac{βIS}{N} - \gamma I$$
$$\frac{dR}{dt}= \gamma I$$
where $\beta$ is the number of people infected at each timestep and $\gamma$ is the recovery rate.  $S$ is the stock of susceptible population, $I$ is the stock of infected, $R$ is the stock of removed population (either by death or recovery), and $N$ is the sum of these three.

The model takes information about the healthy and infected people and simply forecasts the next values based on the ODE system.

**Training process** Scipy library can be used to calculate ODE’s and fit the SIR parameters (e.g curvefit method in the scipy.optimize module).

**Limitations** The SIR model does not count many factors and its parameters are considered to be constant. Death predictions The SIR model is not able to predict death cases.


## SIR with polynomial contact rate (SIR-poly)

SIR-poly model takes population, infected cases, recovered cases as input. The model is able to give predictions for an arbitrary time period. As an output, it gives the number of infected and recovery cases.

**Model description** In the basic SIR model we assume a static contact and transition rates through the entire course of the disease, which is not the case for the epidemics. The spread of the disease has led to large changes in societal behavior and so on, which affect the rate of the spread. It is suggested (Conley, 2020) to define the contact
rate as a function of active cases. For example, let $X_i$ be active cases per thousand $\beta_i$ be the contact rate at a point in time $i$.
$$X_i = \frac{l_i}{N} * 1000$$
$$\beta_i = \beta_aX_i + \beta_b$$
$\beta_i$ is then used as a beta in the basic SIR system.

**Training process** Scipy library can be used to calculate ODE’s and fit the SIR parameters (e.g curvefit method in the scipy.optimize module).

**Limitations** This model does not count many factors. Death predictions The SIR-poly model is not able to predict death cases.

## Influence Models
* Independent Cascade
	* $p_{v,w}$ for each edge
	* SI# if $p_{v,w} = p$
* Linear Threshold
	* $\sum{w_{ij}} > \theta$
	
https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology

https://publications.hse.ru/en/chapters/210598897

  

https://www.researchgate.net/publication/223990697_Competition_among_memes_in_a_world_with_limited_attention

  

[A COVID-19-Based Modified Epidemiological Model and Technological Approaches to Help Vulnerable Individuals Emerge from the Lockdown in the UK

](https://www.researchgate.net/publication/344042984_A_COVID-19-Based_Modified_Epidemiological_Model_and_Technological_Approaches_to_Help_Vulnerable_Individuals_Emerge_from_the_Lockdown_in_the_UK?enrichId=rgreq-e98638d13f27367d73afe51e486c194a-XXX&enrichSource=Y292ZXJQYWdlOzM0NDA0Mjk4NDtBUzo5MzEyNTk2MjY4NDQxNjJAMTU5OTA0MTAwNTc3MA%3D%3D&el=1_x_2&_esc=publicationCoverPdf)

[The Hidden Geometry of Complex, Network-Driven Contagion Phenomena](https://www.researchgate.net/publication/259322075_The_Hidden_Geometry_of_Complex_Network-Driven_Contagion_Phenomena)

  

* Epidemics on networks with NetworkX and EoN [github](https://github.com/Mercurialll/tutors_and_projs/blob/master/jupyter_english/tutorials/Epidemics_on_networks_with_NetworkX_and_EoN_Syrovatskiy_Ilya.ipynb)

  
  
  

# Information propagation

### Inf2vec: Latent Representation Model for Social Influence Embedding
[ieee](https://ieeexplore.ieee.org/document/8509310), [pdf](https://dl.dropboxusercontent.com/s/hn22yzwdei0lc71/inf2vec.pdf)
Авторы предлагают модель для эмбеддинга social influence.
Эмбеддинг происходит следующим образом:

1. Для каждого юзера определяются два influence context: локальный и глобальный. Локальный контекст, это набор пользователей, полученный с помощью random-walk по propagation network, глобальный - набор юзеров, похожих по совершаемым действиям.
2. Эмбеддинг состоит из двух частей (два вектора): -
    1. Source Embedding - отвечающий за способность юзера влиять на других (S)
    2. Target Embedding - отвечающий за то насколько пользователь подвержен влиянию (T)
    3. байасы - influenceability и conformity
3. По контекстам и цепочкам экшонов для пар юзеров считаются вероятности влияния одного юзера на другого, вероятность считается через комбинацию S, T, biases, таким образом вектора фиттятся.

[feng2018.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65ba9b1f-cf93-438e-9fa4-cc7bb7a87103/feng2018.pdf)

  

Inf2Vec model improvement + Influence Maximization task

  

Применение модели из прошлой статьи к задаче максимизации влияния.

  

Принципиально авторы не вносят в модель изменения, только обнаруживают, что для их задачи достаточно смотреть только на юзеров, которые в основном начинают активности, также они упрощают вычисления (насколько я понял делают облегченную модель, в которой эмбединги не вычисляются)

  

[7319-Article Text-10549-1-10-20200601.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8e0649e-4ca4-4d63-b7fe-645ed4849fc3/7319-Article_Text-10549-1-10-20200601.pdf)

  

Deep Collaborative Embedding (DCE)

  

Автоэнкодер каскадов распространения информации. Сначала там собираются cascading contexts, которые для каждого каскада делают матрицу N*N (N - количество нодов), где значения на [i, j] это потенциальное влияние юзера i на юзера j в рамках данного каскада.

  

Затем для каждого нода собираются вектора их влияния на другие ноды в рамках разных каскадов, и это все подается на вход автоанкодеру, из которого достается эмбеддинг для нода.

  

[10.1016@j.knosys.2020.105502.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edca08d7-81a8-40b2-82a2-5d01083516aa/10.1016j.knosys.2020.105502.pdf)


[https://github.com/geopanag/awesome-influence-maximization-papers/blob/master/readme.md](https://github.com/geopanag/awesome-influence-maximization-papers/blob/master/readme.md)

## Tools:
- [ndlib](https://ndlib.readthedocs.io/en/latest/)
- [DEMMO](https://github.com/Paul-NP/demmo/blob/master/help/DEMMo_help.pdf), [habr article](https://habr.com/ru/articles/551682/)

## Colabs
- [Epidemics on networks](https://drive.google.com/file/d/1HadieLdxb8Tjnn8I4-6nDDtgLLaIVuWC/view?usp=sharing)
- [Diffusion Models](https://drive.google.com/file/d/1HJkkts1MEbqo3mI-86C-UfslQCjypqjg/view?usp=sharing)
- [Threshold Models](https://colab.research.google.com/drive/1H_9yopWHGPKF3N4VGp7aR-DzckdQSgEh)
- [SIR + ndlib](https://drive.google.com/file/d/1HLZ_7WIQQ_mpxth-dlafQVOS3rybUHiG/view?usp=sharing)
- [Dummy Covid model](https://drive.google.com/file/d/1HW941aXbF5nPsSO3mmoAJqzPNtyB8L3I/view?usp=sharing)
- [Marketing campaign](https://drive.google.com/file/d/1HTDMz2qvezKvzmKhqqpuG3a5xnSK9PUW/view?usp=sharing)

## References
- Zhukov, D., Khvatova, T., Lesko, S., Zaltsman, A. (2018). Managing social networks: applying Percolation theory methodology to understand individuals’ attitudes and moods. Technological Forecasting and Social Change, Volume 129, April 2018, pp. 297-307.
- A nontrivial interplay between triadic closure, preferential, and anti-preferential attachment: New insights from online data, [Online Social Networks and Media](https://www.sciencedirect.com/science/article/abs/pii/S2468696423000071?dgcid=coauthor), 2023
* CitationIE: Leveraging the Citation Graph for Scientific Information Extraction [pdf](https://arxiv.org/pdf/2106.01560.pdf)
* [VigDet: Knowledge Informed Neural Temporal Point Process for Coordination Detection on Social Media](https://arxiv.org/abs/2110.15454)
