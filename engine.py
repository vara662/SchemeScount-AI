import json

def load_schemes(path="schemes.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def check(scheme: dict, p: dict) -> dict:
    reasons, status = [], "eligible"

    def fail(msg):
        nonlocal status
        status = "not_eligible"
        reasons.append("✗ " + msg)

    def unknown(msg):
        nonlocal status
        if status != "not_eligible":
            status = "needs_info"
        reasons.append("? " + msg)

    if scheme["max_income"] is not None:
        if p["income"] is None:
            unknown("Income not provided")
        elif p["income"] <= scheme["max_income"]:
            reasons.append(f"✓ Income ₹{p['income']:,} is within the limit of ₹{scheme['max_income']:,}")
        else:
            fail(f"Income ₹{p['income']:,} exceeds the limit of ₹{scheme['max_income']:,}")

    if scheme["gender"]:
        if not p["gender"]:
            unknown("Gender not provided")
        elif p["gender"] == scheme["gender"]:
            reasons.append("✓ Gender requirement satisfied")
        else:
            fail(f"Scheme is for {scheme['gender']} applicants")

    if scheme["min_age"] is not None:
        if p["age"] is None:
            unknown("Age not provided")
        elif p["age"] >= scheme["min_age"]:
            reasons.append(f"✓ Age {p['age']} meets minimum {scheme['min_age']}")
        else:
            fail(f"Age {p['age']} is below minimum {scheme['min_age']}")

    if scheme["districts"]:
        if not p["district"]:
            unknown("District not provided")
        elif p["district"] in scheme["districts"]:
            reasons.append("✓ District requirement satisfied")
        else:
            fail("District not covered")

    if scheme["communities"]:
        if not p["community"]:
            unknown("Community not provided")
        elif p["community"] in scheme["communities"]:
            reasons.append("✓ Community requirement satisfied")
        else:
            fail("Community not covered")

    return {"scheme": scheme, "status": status, "reasons": reasons}

def evaluate(profile: dict):
    return [check(s, profile) for s in load_schemes()]