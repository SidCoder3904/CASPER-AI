class keyword :
    WAKEWORD = ['casper', 'kasper', 'gasper', 'gaspar', 'kaspar',
        'caspar', 'cantor', 'castor', 'caster', 'capital', 'despia', 'crystal'] #spell errors
    ww = ['wakeword', 'wake word', 'fake word', 'fakeword', 'wake world', 'wakeworld', 'breakword', 'break word', 'liquid']
    change_ww = ['change', 'convert', 'new', 'shift', 'edit', 'set']
    disable_ww = ['dont', 'disable', 'don\'t', 'not', 'stop', 'do not', 'no']
    enable_ww = ['use', 'enable', 'start']
    
    SLEEP = ['sleep', 'snooze', 'shut down', 'bye']
    
    OPEN = ['open', 'play', 'run', 'start', 'launch', 'search', 'surf']
    CLOSE = ['close', 'kill', 'stop', 'end']
    OPEN_CLOSE = OPEN + CLOSE
    app_dir = {
        ('whatsapp', 'whats app', 'what app', 'what\'sapp') : 'WhatsApp',
        ('spotify', 'music', 'song', 'songs') : 'Spotify',
        ('vscode', 'v s code', 'vs code') : 'Visual Studio Code',
        ('my folder', 'master folder', 'sid') : 'sid',
        (' ppt ', 'powerpoint', 'power point') : 'PowerPoint',
        ('canva', 'canve', 'canvas') : 'Canva',
        (' ps ', ' p s ', 'photoshop', 'photo shop') : 'Adobe Photoshop',
        ('youtube', 'utube', 'you tube', ' yt ', ' y t ') : 'YouTube',
        ('google', 'chrome', 'goggle', ' net ', 'new tab', 'browser') : 'Google Chrome',
        ('settings', 'controls', 'setting') : 'Settings'}
    
    EMAIL = ['email', 'mail', 'gmail']
    add_dir = {
        'myself' : 'siddharthverma3904@gmail.com',
        'mom' : 'lavitavermapdd@gmail.com',
        'samarth' : '2022csb1118@iitrpr.ac.in',
        'ojas' : '2022csb1099@iitrpr.ac.in'}
    
    website_dir = {
        ('classroom', 'class room') : 'https://classroom.google.com/u/2/h',
        ('chatgpt', 'chat gpt', 'chat g p t') : 'https://chat.openai.com/chat',
        ('github', 'git hub', 'gethub', 'get hub', 'getup', 'get up') : 'https://github.com/',
        ('desmos', 'des moss') : 'https://www.desmos.com/calculator'}

    TIME = ['time', ' tine ']
    DATE = ['date', 'day', 'today']
    CAL = ['calendar', 'calender']
    DTC = TIME + DATE + CAL
    
    JOKE = ['joke', 'laugh', 'funny']
