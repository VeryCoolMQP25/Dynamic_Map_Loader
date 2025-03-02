import rclpy
from rclpy.node import Node
from nav2_msgs.srv import LoadMap
import os

class MapLoaderNode(Node):
    def __init__(self):
        super().__init__('map_loader_node')
        self.cli = self.create_client(LoadMap, '/map_server/load_map')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for map_server/load_map service...')
        self.get_logger().info('Connected to map_server/load_map service')

    def load_map(self, map_file_path):
        if not os.path.exists(map_file_path):
            self.get_logger().error(f'Map file does not exist: {map_file_path}')
            return
        request = LoadMap.Request()
        request.map_url = map_file_path
        self.get_logger().info(f'Loading map from {map_file_path}')
        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Map loaded successfully')
        else:
            self.get_logger().error('Failed to load map')

def main(args=None):
    rclpy.init(args=args)
    node = MapLoaderNode()
    node.load_map('/home/tori/Maps/floor4.yaml')  
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
