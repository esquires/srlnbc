import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# you can see what safety_gymnasium uses in
# safety_gymnasium/bases/base_task.py in the self._obstacles information 
# the particular values are filled throughout via
# - safety_gymnasium/tasks/safe_navigation/goal/goal_level1.py
#       extents: how far large the placement space can be
#       keepout: how far other things need to be
# see other defaults in
#   safety_gymnasium/assets/geoms/goal.py (and hazards.py)

point_goal_config = {
    'constrain_hazards': True,
    'goal_keepout': 0.305,  # 0.305
    'goal_size': 0.3,
    'hazards_keepout': 0.18,  # 0.18
    'hazards_num': 8,
    'hazards_size': 0.2,
    'lidar_max_dist': 3,
    'lidar_num_bins': 16,
    # observe_box_lidar: True,
    # observe_goal_lidar: True,
    # observe_hazards: True,
    # observe_vases: True,
    # placements_extents: [-1.5, -1.5, 1.5, 1.5]
    'robot_base': os.path.join(BASE_DIR, 'xmls/point.xml'),
    'action_scale': [1.0, 0.05],  # 1, 1
    'task': 'goal',
    'lidar_alias': True,  # not in cfg
    'constrain_indicator': True,  # not in cfg
    'hazards_cost': 1.0,  # not in cfg
    # vases_num: 1,
    '_seed': None
}

car_goal_config = {
    **point_goal_config,
    'robot_base': 'xmls/car.xml',
    'action_scale': [1.0, 0.02],
}

doggo_goal_config = {
    **point_goal_config,
    'robot_base': 'xmls/doggo.xml',
    'action_scale': 1.0,
    'hazards_num': 2,
    'hazards_size': 0.1,
    'hazards_keepout': 0.5,
    'goal_keepout': 0.5,
    'sensors_obs': 
        ['accelerometer', 'velocimeter', 'gyro', 'magnetometer'] +
        [
            'touch_ankle_1a', 'touch_ankle_2a', 
            'touch_ankle_3a', 'touch_ankle_4a',
            'touch_ankle_1b', 'touch_ankle_2b', 
            'touch_ankle_3b', 'touch_ankle_4b'
        ]
}

point_goal_config_simple = {
    'robot_base': os.path.join(BASE_DIR, 'xmls/point.xml'),
    'action_scale': [1.0, 0.05],

    'task': 'goal',

    'lidar_num_bins': 16,
    'lidar_alias': False,

    'constrain_hazards': True,
    'constrain_indicator': False,

    'hazards_num': 1,
    'hazards_keepout': 1.1,
    'hazards_size': 1.0,
    'hazards_cost': 3.0,
    'hazards_locations': [[0.0, 0.0]],

    'robot_keepout': 0.1,
    'goal_keepout': 0.3,
    'goal_size': 0.2,

    # SimpleEngine specific
    'observe_hazards_pos': True,

    '_seed': None
}
