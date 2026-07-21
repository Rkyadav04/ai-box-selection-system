from typing import Dict, List

from apps import boxes
from apps.boxes.models import ShippingBox
from apps.orders.models import Order

from .exceptions import NoSuitableBoxFound

class  BoxRecommendationService:

    def recommend(self, order: Order) -> ShippingBox:
        
        requirements = self.calculate_requirements(order)

        compatible_boxes = self.find_compatible_boxes(requirements)

        return self.select_best_box(compatible_boxes)
    
    def calculate_requirements(self, order: Order) -> Dict:


        dimensions = order.get_packing_dimensions()

        return {
            **dimensions,
            "weight": order.get_total_weight(),
        }
    def find_compatible_boxes(self, requirements: Dict) -> List[ShippingBox]:

        compatiable_boxes = []

        boxes = ShippingBox.objects.all()

        for box in boxes:

            if (
                box.length >= requirements["length"] and
                box.width >= requirements["width"] and
                box.height >= requirements["height"] and
                box.max_weight >= requirements["weight"]
            ):
                compatiable_boxes.append(box)

        return compatiable_boxes
        
    def select_best_box(self, boxes: List[ShippingBox],) -> ShippingBox:
        if not boxes:
            raise NoSuitableBoxFound("No suitable box found for the given products.")
        return min(boxes, key=lambda box: box.cost)
        

            