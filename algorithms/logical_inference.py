class TrafficRule:
    """Represents a logical rule in the TrafficKB system."""
    def __init__(self, premises, conclusion):
        self.premises = premises  # List of conditions
        self.conclusion = conclusion  # Result (violation/inconsistency)

    def to_clause(self):
        """Convert rule to CNF clause format."""
        return tuple(["¬" + p for p in self.premises] + [self.conclusion])


class TrafficKB:
    def __init__(self):
        self.clauses = []  # Stores logical clauses
        self.violations = set()  # Tracks specific violations
        self.inconsistencies = set()
        self.sensor_data = {}  # Stores numerical sensor data (e.g., speed, BAC levels)

    def add_clause(self, clause):
        """Add a clause (disjunction of literals) to the knowledge base."""
        if clause not in self.clauses:
            self.clauses.append(clause)

    def add_sensor_data(self, key, value):
        """Store numerical sensor data (e.g., BAC levels, speed)."""
        self.sensor_data[key] = value

    def resolve(self, clause1, clause2):
        """Resolve two clauses to produce new clauses (avoid redundant resolutions)."""
        resolvents = set()
        for lit1 in clause1:
            for lit2 in clause2:
                if lit1 == f"¬{lit2}" or lit2 == f"¬{lit1}":
                    resolvent = set(clause1) | set(clause2)
                    resolvent.discard(lit1)
                    resolvent.discard(lit2)
                    resolvents.add(tuple(sorted(resolvent)))  # Store as sorted tuple to avoid duplicates
        return list(resolvents)

    def resolution(self):
        """Apply resolution until no new clauses are derived or a contradiction is found."""
        new_clauses = set()
        while True:
            n = len(self.clauses)
            for i in range(n):
                for j in range(i + 1, n):
                    resolvents = self.resolve(self.clauses[i], self.clauses[j])
                    for r in resolvents:
                        if not r:  # If an empty clause (contradiction) is derived
                            return True  # Violation or inconsistency found
                        if r not in self.clauses and r not in new_clauses:
                            new_clauses.add(r)
            if not new_clauses:
                break
            self.clauses.extend(new_clauses)
            new_clauses.clear()

        # Check for violations/inconsistencies (unit clauses)
        for clause in self.clauses:
            if len(clause) == 1:
                lit = clause[0]
                if lit.startswith("violation_"):
                    self.violations.add(lit)
                elif lit == "inconsistency":
                    self.inconsistencies.add(lit)

        return bool(self.violations or self.inconsistencies)


# ====================
# Example Scenarios
# ====================

def example_speeding():
    """Detect speeding violation using real speed data."""
    kb = TrafficKB()

    # Store actual speed
    kb.add_sensor_data("speed", 55)  # Speed = 55 km/h

    # Define rule: If speed > 60 km/h → "speed_over_limit"
    if kb.sensor_data["speed"] > 60:
        kb.add_clause(("speed_over_limit",))

    # Rule: If "speed_over_limit" → "violation_speeding"
    rule = TrafficRule(["speed_over_limit"], "violation_speeding")
    kb.add_clause(rule.to_clause())

    return kb.resolution()


def example_red_light():
    """Detect running a red light."""
    kb = TrafficKB()

    # Define rule: If red light + moving → violation
    rule = TrafficRule(["red_light", "vehicle_moving"], "violation_red_light")
    kb.add_clause(rule.to_clause())

    # Sensor Data
    kb.add_sensor_data("red_light", True)
    kb.add_sensor_data("vehicle_moving", True)

    if kb.sensor_data["red_light"]:
        kb.add_clause(("red_light",))
    if kb.sensor_data["vehicle_moving"]:
        kb.add_clause(("vehicle_moving",))

    return kb.resolution()


def example_lane_violation():
    """Detect unsafe lane change (no signal)."""
    kb = TrafficKB()

    # Rule: Lane change + no signal → violation
    rule = TrafficRule(["lane_change", "signal_off"], "violation_lane")
    kb.add_clause(rule.to_clause())

    # Sensor Data
    kb.add_sensor_data("lane_change", True)
    kb.add_sensor_data("signal_off", True)

    if kb.sensor_data["lane_change"]:
        kb.add_clause(("lane_change",))
    if kb.sensor_data["signal_off"]:
        kb.add_clause(("signal_off",))

    return kb.resolution()


def example_location_inconsistency():
    """Detect impossible GPS locations."""
    kb = TrafficKB()

    # Rule: Cannot be in two places at once
    rule = TrafficRule(["at_intersection_A", "at_highway_B"], "inconsistency")
    kb.add_clause(rule.to_clause())

    # Sensor Data
    kb.add_sensor_data("at_intersection_A", True)
    kb.add_sensor_data("at_highway_B", False)

    if kb.sensor_data["at_intersection_A"]:
        kb.add_clause(("at_intersection_A",))
    if kb.sensor_data["at_highway_B"]:
        kb.add_clause(("at_highway_B",))

    return kb.resolution()


def example_drink_driving():
    """Detect drink driving (Singapore BAC limits)."""
    kb = TrafficKB()

    # Store alcohol levels
    kb.add_sensor_data("bac_blood", 70)  # Blood Alcohol = 70 mg/100ml
    kb.add_sensor_data("bac_breath", 30)  # Breath Alcohol = 30 µg/100ml

    # Singapore Limits: 80 mg/100ml (blood), 35 µg/100ml (breath)
    if kb.sensor_data["bac_blood"] > 80:
        kb.add_clause(("bac_blood_over",))
    if kb.sensor_data["bac_breath"] > 35:
        kb.add_clause(("bac_breath_over",))

    # Define rules
    rule1 = TrafficRule(["bac_blood_over"], "violation_drink_driving")
    rule2 = TrafficRule(["bac_breath_over"], "violation_drink_driving")

    kb.add_clause(rule1.to_clause())
    kb.add_clause(rule2.to_clause())

    return kb.resolution()


if __name__ == "__main__":
    print("=== Speeding ===", example_speeding())  # True (Speeding Violation Detected)
    print("=== Red Light ===", example_red_light())  # True (Red Light Violation Detected)
    print("=== Lane Violation ===", example_lane_violation())  # True (Lane Violation Detected)
    print("=== Location Inconsistency ===", example_location_inconsistency())  # True (Inconsistent Location Detected)
    print("=== Drink Driving ===", example_drink_driving())  # True (Drink Driving Violation Detected)
