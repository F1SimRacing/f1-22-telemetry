# F1 22 Telemetry

# Main Source for this Project
The F1 22 UDP specification is available [here](https://answers.ea.com/t5/General-Discussion/F1-22-UDP-Specification/td-p/11551274?attachment-id=607611)

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
