def calculate_timeline(m1, m2, initial_v1, b1_size, b2_size, wall_x):
    v1 = initial_v1
    v2 = 0
    x1 = 1
    x2 = -1
    
    events = []
    total_collisions = 0
    
    while not (v2 >= 0 and v1 >= v2):
        current_v1 = v1
        current_v2 = v2
        
        if v2 < 0:
            t_w = max(0.0, (wall_x - (x2 - b2_size/2)) / v2)
        else:
            t_w = float('inf')
            
        if v1 < v2:
            t_b = max(0.0, ((x2 + b2_size/2) - (x1 - b1_size/2)) / (v1 - v2))
        else:
            t_b = float('inf')
        
        t = min(t_w, t_b)
        
        
        x1 += v1 * t
        x2 += v2 * t
        total_collisions += 1
       
        if t == t_w:
            v2 *= -1.0
            impact = "wall"
        else:
            v1_new = ((m1 - m2)*v1 + 2*m2*v2) / (m1 + m2)
            v2_new = (2*m1*v1 + (m2 - m1)*v2) / (m1 + m2)
            v1 = v1_new
            v2 = v2_new
            impact = "block"
            
        events.append({
            "collision": total_collisions,
            "impact": impact,
            "time_delta": t,              # Required for Manim run_time
            "v1_during": current_v1,      # Required for Manim block 1 shift
            "v2_during": current_v2,      # Required for Manim block 2 shift
            "v1": v1,                     # Required for terminal printout
            "v2": v2                      # Required for terminal printout
        })
    
    
    return events, total_collisions


if __name__ == "__main__":
    n = 3 # how many decimal points of pi
    mass_1 = 100**n
    mass_2 = 1
    velocity_1 = -2
    size_1, size_2 = 1.2, 0.6
    wall_position = -4
    
    print(f"Running physics engine. m1={mass_1}, m2={mass_2}")
    
    timeline_data, collisions = calculate_timeline(
        mass_1, mass_2, velocity_1, size_1, size_2, wall_position
    )
    
    print(f"Simulation complete. Total collisions calculated: {collisions} \n Pi estimate: {collisions / (10**n)}")
    
    
    #for event in timeline_data:
        #print(f"#{event['collision']} | Hit: {event['impact']} | v1: {event['v1']:.2f} | v2: {event['v2']:.2f}")