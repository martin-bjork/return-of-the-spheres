from pygame.locals import *
# NOTE: Ugly namespace polution, but safer than using eval() to
# associate strings with the right pygame key constant.

class Profile:
    ''' The current profile containing player preferences.'''

    def __init__(self, configDict):
        assert isinstance(configDict, dict)
        assert 'visual' in configDict, \
            "The supplied configuration file must have all the needed \
                information"
        assert 'control' in configDict, \
            "The supplied configuration file must have all the needed \
                information"
        assert 'debug' in configDict, \
            "The supplied configuration file must have all the needed \
                information"

        self._main = configDict
        self._visual = configDict['visual']
        self._control = configDict['control']
        self._debug = configDict['debug']

        assert isinstance(self._visual, dict), "The config file is faulty"
        assert isinstance(self._control, dict), "The config file is faulty"
        assert isinstance(self._debug, dict), "The config file is faulty"

   
    def _convert_to_pygame_keys(self, key_list):
        ''' Format according to the pygame constant naming.
        The fetch the actual constant value from the local variable pool.'''
        # single letter keys are denoted 'K_<letter>', whereas all
        # the other keys are denoted 'K_<KEY_NAME>'
        keys = key_list[:]

        for i in range(len(keys)):
            if keys[i] == None:
                continue
            elif len(keys[i]) == 1:
                keys[i] = globals()['K_' + keys[i].lower()]
            else:
                keys[i] = globals()['K_' + keys[i].upper()]

        return keys

    def get_keys(self, action):
        assert action in self._control, 'The specified action is not defined.'

        keys = self._control[action]
        return self._convert_to_pygame_keys(keys)

    def set_keys(self, action, keys):
        assert action in self._control, 'The specified action is not defined.'
        assert len(keys) == 2, 'You must supply two values for the action.'

        self._control[action] = keys
    
    def get_mouse_sensitivity(self):
        return self._control['mouse_sensitivity']

    def set_mouse_sensitivity(self, sens):
        assert isinstance(sens, float)

        self._control['mouse_sensitivity'] = sens

    def has_fullscreen(self):
        return self._visual['fullscreen']

    def current_width(self):
        if self.has_fullscreen():
            return self._visual['fullscreen_width']
        else:
            return self._visual['window_width']

    def current_height(self):
        if self.has_fullscreen():
            return self._visual['fullscreen_height']
        else:
            return self._visual['window_height']

    def get_fullscreen_width(self):
        return self._visual['fullscreen_width']

    def get_fullscreen_height(self):
        return self._visual['fullscreen_height']

    def get_window_width(self):
        return self._visual['window_width']

    def get_window_height(self):
        return self._visual['window_height']

    def set_fullscreen_width(self, width):
        self._visual['fullscreen_width'] = width

    def set_fullscreen_height(self):
        self._visual['fullscreen_height'] = height

    def set_window_width(self, width):
        self._visual['window_width'] = width

    def set_window_height(self):
        self._visual['window_height'] = height

    def is_debugging(self):
        return self._debug['debug_mode']

    def set_debugging(self, option):
        assert isinstance(option, bool)
        self._debug['debug_mode'] = option
