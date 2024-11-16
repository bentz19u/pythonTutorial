test = {
    'input': {
        'root': {
            'info': 3,
            'left': {
                'info': 2,
                'left': {
                    'info': 1,
                    'left': None,
                    'right': None,
                },
                'right': None,
            },
            'right': {
                'info': 5,
                'left': {
                    'info': 4,
                    'left': None,
                    'right': None,
                },
                'right': {
                    'info': 6,
                    'left': None,
                    'right': {
                        'info': 7,
                        'left': None,
                        'right': None,
                    },
                },
            },
        }
    },
    'output': True
}

tests = [
    {
        'input': {
            'root': {
                'info': 4,
                'left': {
                    'info': 2,
                    'left': {
                        'info': 1,
                        'left': None,
                        'right': None,
                    },
                    'right': {
                        'info': 3,
                        'left': None,
                        'right': None,
                    },
                },
                'right': {
                    'info': 6,
                    'left': {
                        'info': 5,
                        'left': None,
                        'right': None,
                    },
                    'right': {
                        'info': 7,
                        'left': None,
                        'right': None,
                    },
                },
            }
        },
        'output': True
    },
    {
        'input': {
            'root': {
                'info': 3,
                'left': {
                    'info': 2,
                    'left': {
                        'info': 1,
                        'left': None,
                        'right': None,
                    },
                    'right': None,
                },
                'right': {
                    'info': 5,
                    'left': {
                        'info': 4,
                        'left': None,
                        'right': None,
                    },
                    'right': {
                        'info': 6,
                        'left': None,
                        'right': {
                            'info': 1,
                            'left': None,
                            'right': None,
                        },
                    },
                },
            }
        },
        'output': False
    },
    {
        'input': {
            'root': {
                'info': 4,
                'left': {
                    'info': 2,
                    'left': {
                        'info': 1,
                        'left': None,
                        'right': None,
                    },
                    'right': {
                        'info': 3,
                        'left': None,
                        'right': None,
                    },
                },
                'right': {
                    'info': 6,
                    'left': {
                        'info': 1,
                        'left': None,
                        'right': None,
                    },
                    'right': {
                        'info': 7,
                        'left': None,
                        'right': None,
                    },
                },
            }
        },
        'output': False
    },
]