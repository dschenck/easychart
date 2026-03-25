def deduplicate(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]