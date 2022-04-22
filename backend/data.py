import random

def get(stream_id: int, event_id: int) -> int:
   generator = random.Random()
   generator.seed(stream_id * event_id)
   
   return generator.randrange(1000)