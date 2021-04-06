import requests
import json


def get_result(url):
    """
    Function that calculates the bowling score provided from a RESTapi and posts the result.
    Returns a string of "success" if the score is correct else "failure".
    """

    api_request = requests.get(url)

    score = json.loads(api_request.text)

    total = [0]

    for idx, frame in enumerate(score['points']):
        # Check if not on last frame
        if len(score['points'])-1 != idx:
            # Check for strike
            if frame[0] == 10:
                if score['points'][idx+1][0] == 10 and score['points'][idx+1][1] == 10:
                    total.append(total[-1] + frame[0] + score['points'][idx+1][0] + score['points'][idx+1][1])
                elif score['points'][idx+1][0] == 10:
                    total.append(total[-1] + frame[0] + score['points'][idx+1][0] + score['points'][idx+2][0])
                else:
                    total.append(total[-1] + frame[0] + score['points'][idx+1][0] + score['points'][idx+1][1])
            # Check for spare
            elif frame[0] + frame [1] == 10:
                total.append(total[-1] + frame[0] + frame[1] + score['points'][idx+1][0])
            else:
                total.append(total[-1] + frame[0] + frame[1])
        # Don't count bonus separately 
        elif len(score['points']) == 11:
            continue
        # If we are on last frame
        else:
            total.append(total[-1] + frame[0] + frame[1])

    # Create the post object
    post_dict = {'token': score['token'],
                'points': total[1:]}

    post_request = requests.post(url, json=post_dict)
    success = json.loads(post_request.text)

    return "Success", total[1:] if success['success'] else "Failure"

print(get_result("http://13.74.31.101/api/points"))