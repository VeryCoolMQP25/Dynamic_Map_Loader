import rclpy
from rclpy.node import Node
from nav2_msgs.srv import LoadMap
from std_msgs.msg import String  # Assuming button presses published as strings

class DynamicMapLoader(Node):
    def __init__(self):
        super().__init__('dynamic_map_loader')
        self.client = self.create_client(LoadMap, '/map_server/load_map')
        self.subscription = self.create_subscription(
            String, '/elevator_button', self.button_callback, 10) # determines button pressed (Vivek publishes to this topic)
        self.get_logger().info("Dynamic Map Loader Node Started")

    def button_callback(self, msg):
        # Map button input to the corresponding map file
        map_dict = {
            "Floor1": "/home/tori/Maps/map_Unity1.yaml",
            "Floor2": "/home/tori/Maps/map_Unity2.yaml",
            "Floor3": "/home/suki/ros2_ws/src/Unity-Coordinates/map_Unity3.yaml",
            "Floor4": "/home/tori/Maps/map_Unity4.yaml",
            "Floor5": "/home/tori/Maps/map_Unity5.yaml",
        }

        map_path = map_dict.get(msg.data, None)

        if map_path:
            self.get_logger().info(f"Button {msg.data} detected. Loading map: {map_path}")
            self.send_request(map_path)
        else:
            self.get_logger().warn(f"No map found for button: {msg.data}")

    def send_request(self, map_path):
        while not self.client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('Waiting for map_server service...')

        request = LoadMap.Request()
        request.map_url = map_path

        future = self.client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Service Response: {response}")
            if response.result:
                self.get_logger().info("Map loaded successfully!")
            else:
                self.get_logger().error("Failed to load map!")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DynamicMapLoader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
