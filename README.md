# F1 22 Telemetry

# Main Source for this Project
To speed up the building of this project, the packet format was taken from
[this](https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/?do=findComment&comment=624274)
post on the Codemasters forums. Which oddly works for F1 22, which is nice.

Thanks to the hard work of the poster I was able to skip the tedious packet decoding.

The updated F1 22 UDP specification is available [here](https://answers.ea.com/t5/General-Discussion/F1-22-UDP-Specification/td-p/11551274?attachment-id=607611)

# Installing

```commandline
pip install f1-22-telemetry
```

# Running
```commandline
telemetry-f1-22-listener
```

# Usage

```python
from f1_22_telemetry.listener import TelemetryListener

listener = TelemetryListener(port=20777, host='localhost')
packet = listener.get()
```

# Releasing
```commandline
pip install --upgrade build twine
python -m build
python3 -m twine upload f1-22-telemetry
```
