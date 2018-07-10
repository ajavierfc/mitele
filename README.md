This script is idented to play live broadcast content from mitele.es

Require requests

# Usage

_Choose channel and play (check the player path in the source)_

`./get.py`

_Get link channel (must be used within the script session, see example below)_

`./get.py <telecinco|cuatro|boing|divinity|fdf|energy|bemad|futbol-mitele>`

_Player_

Default player command is 'mpv', under windows you may want to use vlc, so set the player command as `"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"`

__Examples__

Linux: ``mpv `./get.py boing` ``

Windows (Powershell): `& 'C:\Program Files\VideoLAN\VLC\vlc.exe' (python .\get.py boing)`

__Notes__

* telecinco and cuatro may not work as they need authentication
* outside from spain probably wont work as is, cause to geo-lock

