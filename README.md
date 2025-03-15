# Dynamic Map Loader
Switches between maps depending on button pressed. 
The node uses the service client /map_server/load_map to dynamically update the map. 


## Subscribed to the following topic:
/elevator_button (std_msgs/String)

If the button for floor 4 is pressed for instance, a string formatted as "Floor4" should be published to this topic. 

Here's how to send a message to that topic from the command line: 

 ```  ros2 topic pub /elevator_button std_msgs/msg/String "data: 'Floor4'" --once ```
 
## To run:
```ros2 run map_loader map_loader```
