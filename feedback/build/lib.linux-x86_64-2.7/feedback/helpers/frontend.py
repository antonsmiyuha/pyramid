def get_data(data, key):
    if data is not None:
        try:
            return data.getone(key)
        except KeyError:
            return ''
    return ''


def get_subjects():
    return [
        'First',
        'Second',
        'Third'
    ]


def get_statuses():
    return [
        'new',
        'spam',
        'read',
        'important'
    ]


def selected(value, option):
    if value == option:
        return 'selected'
    else:
        return ''
