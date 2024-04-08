class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            preference = students[0]
            sandwich = sandwiches[0]

            if preference == sandwich:
                students.pop(0)
                sandwiches.pop(0)
            else:
                moveBack = students.pop(0)
                students.append(moveBack)

                if sandwich not in students:
                    # return len(students)
                    break
            # print(f"q = {students}")
            # print(f"s = {sandwiches}")
        return len(students)
        