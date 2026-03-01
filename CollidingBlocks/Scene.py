from manim import *
from Physics import calculate_timeline

class CollidingBlocks(MovingCameraScene):
    def construct(self):
        n = 0 # how many decimal points of pi
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
        labels_group = VGroup(counter_label,count_num)
        
        self.play(
            old_scene.animate.scale(0.7).to_edge(DOWN, buff=0.4),
            labels_group.animate.scale(0.9).to_edge(UP, buff=0.6),
            run_time=2,
            rate_func=smooth
        )
        
     
        self.play(FadeOut(count_num), run_time=0.5)
        count_num.set_value(0)
        
        coordinate_grid = NumberPlane(
        x_range=[-1.25, 1.25, 0.5], 
         y_range=[-1.25, 1.25, 0.5], 
        x_length=3.75, 
        y_length=3.75,
        background_line_style={"stroke_color": WHITE, "stroke_width": 1}
            )
        

        self.play(
            Create(coordinate_grid), 
            run_time=1.5, 
            rate_func=smooth
            )
        
        main_circle = Circle(radius=1.5, color=WHITE)
        
  
        self.play(
            Create(main_circle),
            FadeIn(count_num),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(
            main_circle.animate.shift(UP*0.5),
            coordinate_grid.animate.shift(UP*0.5),
            run_time=1.5,
            rate_func=smooth
            )
        
        radius_line = Line(start=ORIGIN, end=RIGHT*1.5, color=WHITE, stroke_width=5,).shift(UP*0.5)
        radius_label = MathTex("1").next_to(radius_line, UP, buff=0.1)
        
        self.play(
             Create(radius_line),
             Write(radius_label),
             run_time=1
             )

        law1 = MathTex(r"P = m_1 v_1 + m_2 v_2").to_edge(LEFT, buff=0.5).scale(0.75)
        law1_label = Text("Conservation of Momentum", color=BLUE).next_to(law1, UP, buff=0.3).scale(0.5)
        law1_box = SurroundingRectangle(law1, color=BLUE, buff=0.2)

        self.play(
            FadeIn(law1_label),
            FadeIn(law1_box),
            run_time=1
        )

        self.play(
            Write(law1),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)

        self.play(
            FadeOut(law1),
            FadeOut(law1_label),
            FadeOut(law1_box),
             run_time=1
        )

        law1.to_edge(UP, buff = 1)

        self.play(
            FadeIn(law1),
            runtime = 0.5
        )


        law2 = MathTex(r"E = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2").to_edge(LEFT, buff=0.5).scale(0.75)
        law2_label = Text("Conservation of Energy", color=BLUE).next_to(law2, UP, buff=0.3).scale(0.5)
        law2_box = SurroundingRectangle(law2, color=BLUE, buff=0.2)


        self.play(
            FadeIn(law2_label),
            FadeIn(law2_box),
            run_time=1
        )
    
        self.play(
            Write(law2),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)

        self.play(
            FadeOut(law2),
            FadeOut(law2_label),
            FadeOut(law2_box),
             run_time=1
        )
        
        law2.next_to(law1, DOWN, buff=0.5)

        self.play(
            FadeIn(law2),
            runtime = 0.5
        )