## listup_delete_on_termination_false_instanes.py
### print only instances display name
```
python listup_delete_on_termination_false_instanes.py <profile name>  | jq '.[]."Instances"[]."Tags"[] | {"Name": .Value}'
```
