
test_scores = [[[4, 0], [6, 4], [7, 1], [3, 3], [0, 3], [5, 5], [7, 3], [4, 2]],
            [[0, 8], [6, 2]],
            [[2, 3], [0, 8], [0, 8], [8, 0], [6, 0], [8, 1]],
            [[5, 2], [7, 2], [10, 0], [6, 3], [5, 2], [2, 8], [10, 0], [3, 0], [10, 0], [3, 5]],
            [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10]]]




def get_result_only_points(points):
    """
    Same is the main function "get_result" from "bownling.py", but stripped of the requests in order to do unit tests.
    Returns the result that would be the value of "points".
    """
    total = [0]

    for idx, frame in enumerate(points):
        # Check if not on last frame
        if len(points)-1 != idx:
            # Check for strike
            if frame[0] == 10:
                if points[idx+1][0] == 10 and points[idx+1][1] == 10:
                    total.append(total[-1] + frame[0] + points[idx+1][0] + points[idx+1][1])
                elif points[idx+1][0] == 10:
                    total.append(total[-1] + frame[0] + points[idx+1][0] + points[idx+2][0])
                else:
                    total.append(total[-1] + frame[0] + points[idx+1][0] + points[idx+1][1])
            # Check for spare
            elif frame[0] + frame [1] == 10:
                total.append(total[-1] + frame[0] + frame[1] + points[idx+1][0])
            else:
                total.append(total[-1] + frame[0] + frame[1])
        # Don't count bonus separately 
        elif len(points) == 11:
            continue
        # If we are on last frame
        else:
            total.append(total[-1] + frame[0] + frame[1])

    # Create the post object
    return total[1:]

def test_get_results():
    assert get_result_only_points(test_scores[0]) == [4,21,29,35,38,55,69,75]
    assert get_result_only_points(test_scores[1]) == [8,16]
    assert get_result_only_points(test_scores[2]) == [5, 13, 21, 29, 35, 44]
    assert get_result_only_points(test_scores[3]) == [7, 16, 35, 44, 51, 71, 84, 87, 105, 113]
    assert get_result_only_points(test_scores[4]) == [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    assert get_result_only_points(test_scores[4]) != []
    assert get_result_only_points(test_scores[2]) != [4,21,29,35,38,55,69,75]

if __name__ == "__main__":
    test_get_results()
    print("No errors")
