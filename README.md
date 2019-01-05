# rm-gym

RoboMaster AI Challenge Simulation Environment based on [OpenAI gym](https://github.com/openai/gym)

## Environment

### Action Space

a four-dimension array [delta_x, delta_y, shoot, shoot_dir]

### Observation Space

other robots' status

### Reward

A reward of 1 will be given if shooting at other robots is successful.

## Installation

1. Install gym

```bash
pip install gym
```

2. Download this repo and install this package via

```bash
pip install -e .
```

## Usage

```python
import gym
import rm_gym

env = gym.make("RoboMaster-v0")
```

An example can be found [here](https://github.com/0aqz0/gym-examples/tree/master/rmSim).
