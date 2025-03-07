# Dynamic Map Loader
Switches between maps depending on button pressed. 
The node uses the service client /map_server/load_map to dynamically update the map. 


## Subscribed to the following topic:
/elevator_button (std_msgs/String)

If the button for floor 4 is pressed for instance, a string formatted as "Floor4" should be published to this topic. 

## To run:
```ros2 run map_loader map_loader```
