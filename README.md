# rm-gym

RoboMaster AI Challenge Simulation Environment based on [OpenAI gym](https://github.com/openai/gym)

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

## TODO

- add bars in the GUI
- add more funcs in class map
- ~~map2pygame coordinates need conversion~~ 
- ~~improve the step func~~
- ~~finish a astar path planning example~~
