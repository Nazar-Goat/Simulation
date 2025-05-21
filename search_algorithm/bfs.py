class Bfs:
    """Class for finding the shortest path using BFS"""
    
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Возможные направления движения
    
    def bfs_find_path(self, start, is_target, map_obj):
        """
        Find the shortest path from start to the target defined by is_target

        Args:
        start: start coordinates (x, y)
        is_target: function that takes coordinates and returns True if the target is found
        map_obj: map object

        Returns:
        List of coordinates that make up the path from start to the target, or None if the path is not found
        """
        queue = [start]  
        visited = {start: None}  
        
        while queue:
            current = queue.pop(0)
            
            if is_target(current, map_obj):
                path = []
                while current != start:
                    path.append(current)
                    current = visited[current]
                path.reverse()
                return path
            
            for dx, dy in self.directions:
                nx, ny = current[0] + dx, current[1] + dy
                neighbor = (nx, ny)
                
                if (0 <= nx < map_obj.width and 
                    0 <= ny < map_obj.height and 
                    neighbor not in visited):
                    
                    queue.append(neighbor)
                    visited[neighbor] = current
        
        return None  
