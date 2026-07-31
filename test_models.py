from models import SlidePlan, Slide

# should succeed (5 slides)
ok = SlidePlan(slides=[Slide(description="d", narration="n") for _ in range(5)])
print("5 slides ok:", ok)

# should fail (2 slides)
try:
    bad = SlidePlan(slides=[Slide(description="d", narration="n") for _ in range(2)])
    print("BUG: 2 slides should have failed but didn't")
except Exception as e:
    print("2 slides correctly rejected:", e)