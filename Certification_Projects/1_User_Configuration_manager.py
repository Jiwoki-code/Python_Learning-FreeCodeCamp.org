test_settings = {
    "theme": "light",
    "notification": False,
    "volume": 50.0,
    "id": 5001,
}

def add_setting(settings: dict, new_setting: tuple):  
    setting_key = new_setting[0].lower()
    setting_value = new_setting[1].lower()

    if not setting_key in settings.keys():
        _new_setting = (setting_key, setting_value)
        settings.update({_new_setting})
        return f"Setting '{setting_key}' added with value '{setting_value}' successfully!"

    if setting_key in settings.keys():
        return f"Setting '{setting_key}' already exists! Cannot add a new setting with this name."

def update_setting(settings: dict, setting_to_update: tuple):
    setting_key = setting_to_update[0].lower()
    setting_value = setting_to_update[1].lower()
    new_setting = (setting_key, setting_value)

    if setting_key in settings.keys():
        settings.update({new_setting})
        return f"Setting '{setting_key}' updated to '{setting_value}' successfully!"

    if not setting_key in settings.keys():
        return f"Setting '{setting_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, setting_to_remove: str):
    _removed_setting = setting_to_remove.lower()

    if _removed_setting in settings.keys():
        settings.pop(_removed_setting)
        return f"Setting '{_removed_setting}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings: dict):
    if settings == {}:
        return "No settings available."

    settings_view = "Current User Settings:\n"
    for key, value in settings.items():
        settings_view += f"{key.capitalize()}: {value}\n"
    
    return settings_view

update_setting(test_settings, ('theme', 'dark'))
print(view_settings(test_settings))