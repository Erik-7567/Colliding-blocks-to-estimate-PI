from manim import *
from Physics import calculate_timeline

class CollidingBlocks(MovingCameraScene):
    def construct(self):
        n = 2 # how many decimal points of pi
        m1 = 100**n
        m2 = 1.0
        v1_start = -1.0
        b1_size, b2_size = 1.2, 0.6
        wall_x = -4.0
        
        
        timeline, total_collisions = calculate_timeline(m1, m2, v1_start, b1_size, b2_size, wall_x)

        wall = Line(UP*2, DOWN*1).move_to(LEFT*4)
        floor = Line(LEFT*5, RIGHT*5).shift(DOWN*1)
        block1 = Square(side_length=b1_size).set_fill(BLUE, 1).move_to(RIGHT*1.0 + DOWN*(1 - b1_size/2))
        block2 = Square(side_length=b2_size).set_fill(RED, 1).move_to(RIGHT*-1.0 + DOWN*(1 - b2_size/2))
        
        counter_label = Text("Collisions: ").to_edge(UP).shift(LEFT*0.5, DOWN*0.5)
        count_num = Integer(0).next_to(counter_label, RIGHT).shift(DOWN * 0.08)
        self.add(wall, floor, block1, block2, counter_label, count_num)

        for event in timeline:
            
            block1.set_color(BLUE)
            block2.set_color(RED)

            t = event["time_delta"]
            v1_current = event["v1_during"]
            v2_current = event["v2_during"]
            
            
            current_col = event["collision"]
            
            if n == 1:
                sim_speed = max(0.05, t)
            else:
                sim_speed = max(0.01, t)
            
            
            self.play(
                block1.animate.shift(RIGHT * v1_current * t),
                block2.animate.shift(RIGHT * v2_current * t),
                run_time=sim_speed,
                rate_func=linear
            )
            
            
            count_num.set_value(current_col)

       
        final_event = timeline[-1]
        exit_v1 = final_event["v1"]
        exit_v2 = final_event["v2"]


        self.play(
            block1.animate.shift(RIGHT * exit_v1 * 3), 
            block2.animate.shift(RIGHT * exit_v2 * 3), 
            run_time=3,
            rate_func=linear
        )
        
       
        self.play(
            FadeOut(block1, shift=RIGHT * exit_v1 * 1),
            FadeOut(block2, shift=RIGHT * exit_v2 * 1),
            run_time=1,
            rate_func=linear
        )

        
    
        old_scene = VGroup(wall, floor)
        labels_scene = VGroup(counter_label,count_num)
        
        self.play(
            old_scene.animate.scale(0.7).to_edge(DOWN, buff=0.4),
            labels_scene.animate.scale(0.9).to_edge(UP, buff=0.6),
            run_time=2,
            rate_func=smooth
        )
        
     
        self.play(FadeOut(count_num), run_time=0.5)
        count_num.set_value(0)
        
        

        main_circle = Circle(radius=1.5, color=WHITE)
        
  
        self.play(
            Create(main_circle),
            main_circle.animate.shift(UP*0.5),
            FadeIn(count_num),
            run_time=1.5,
            rate_func=smooth
        )
  