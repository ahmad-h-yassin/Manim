from manim import *
import random
#from gpt

class BubbleSortVisualization(Scene):
    def construct(self):
        # Define the array to be sorted
        # Create an empty list to store random numbers
        random_numbers = []

        # Generate 10 random whole numbers between 0 (inclusive) and 100 (exclusive)
        for _ in range(10):
            random_numbers.append(random.randint(1, 20))

        # array = [4, 3, 2, 1, 5]
        array = random_numbers

        num_elements = len(array)

        # Create a list of rectangles for each element in the array
        rects = [Rectangle(height=num/2, width=0.5, fill_color=BLUE, fill_opacity=1) for num in array]

        # Position the rectangles
        for i, rect in enumerate(rects):
            rect.move_to(LEFT * (i - (num_elements - 1) / 2))

        # Add the rectangles to the scene
        self.play(*[Create(rect) for rect in rects])

        # Bubble sort logic with movement animation
        def bubble_sort(arr, elements):
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    # Highlight the element being replaced by changing its color to red
                    elements[j].set_fill(RED)
                    # Swap arr[j] and arr[j+1] if arr[j] > arr[j+1]
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        # Swap the rectangles
                        elements[j], elements[j+1] = elements[j+1], elements[j]
                        # Animate the swapping of elements
                        self.play(elements[j].animate.move_to(elements[j+1].get_center()),
                                 elements[j+1].animate.move_to(elements[j].get_center()),
                                 run_time=0.5)
                    # Revert the color back to blue after the swap is completed
                    elements[j].set_fill(BLUE)
                # Highlight the last element after it's no longer being moved or swapped
                elements[n-i-1].set_fill(GREEN)

        # Perform the bubble sort animation
        bubble_sort(array, rects)

        # Wait before ending the scene
        self.wait()



#from phind


class BubbleSortScene(Scene):
    def construct(self):
        # Define the array to be sorted
        array = [4, 3, 2, 1, 5]

        # Create a list of Text objects for each element in the array
        text_elements = [Text(str(num)).scale(0.5) for num in array]

        # Position the text elements
        for i, text in enumerate(text_elements):
            text.move_to(LEFT * (i - 2) + UP)

        # Add the text elements to the scene
        self.play(*[Create(text) for text in text_elements])

        # Bubble sort logic with movement animation
        def bubble_sort(arr, elements):
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    # Swap arr[j] and arr[j+1] if arr[j] > arr[j+1]
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        # Swap the text elements
                        elements[j], elements[j+1] = elements[j+1], elements[j]
                        # Animate the swapping of elements
                        self.play(elements[j].animate.move_to(elements[j+1].get_center()),
                                 elements[j+1].animate.move_to(elements[j].get_center()),
                                 run_time=0.5)

        # Perform the bubble sort animation
        bubble_sort(array, text_elements)

        # Highlight the sorted elements
        self.play(*[text.animate.set_color(GREEN) for text in text_elements], run_time=1)

        # Wait before ending the scene
        self.wait()

# from gemni
class BubbleSort(Scene):
  def construct(self):
    # Create a list of numbers
    data = [8, 3, 1, 4, 2, 7, 6, 5]
    text_data = VGroup()

    # Create text labels for each number
    for i, num in enumerate(data):
      label = Text(str(num), font_size=24, color=WHITE)
      label.move_to(RIGHT * i)
      text_data.add(label)

    self.add(text_data)

    # Loop through the list for multiple passes
    for i in range(len(data) - 1):
      swapped = False
      for j in range(len(data) - i - 1):
        # Compare adjacent elements
        if data[j] > data[j + 1]:
          swapped = True
          # Swap elements visually
          self.play(FadeOut(text_data[j], text_data[j + 1]))
          data[j], data[j + 1] = data[j + 1], data[j]
          self.play(FadeIn(text_data[j].move_to(RIGHT * j), text_data[j + 1].move_to(RIGHT * (j + 1))))
      # No swaps in a pass means the list is sorted
      if not swapped:
        break

    self.wait(1)  # Wait for a moment after sorting
