import requests
import time
from twilio.rest import TwilioRestClient


def get_trimet_response(location_id="7782"):
    """Send a request to the TriMet API requesting the arrival times
    for location_id.  Return the response in JSON format."""
    url = "https://developer.trimet.org/ws/v2/arrivals"
    parameters = {"locIDs": location_id, "appID": "14BBB####################", "json": "true", "minutes": "60"}
    response = requests.get(url, parameters)
    return response.json()


def get_arrivals(response):
    """From a TriMet response message get the container that holds
    all the arrivals from the message"""
    if "resultSet" in response.keys() and \
       "arrival" in response["resultSet"].keys():
            arrivals = response["resultSet"]["arrival"]
    return arrivals


def get_arrival_times(arrivals):
    """From a dictionary of arrivals get the route and estimated time
    for each arrival"""
    arrival_times = []
    for arrival in arrivals:
        if "estimated" in arrival.keys():
            arrival_times.append((arrival["route"], arrival["estimated"]))
    return arrival_times


def get_bus_arrival_times(arrival_times, bus_number=19):
    """arrival_times is a list of tuples with the following format:
    (bus_number, arrival_time).  Function returns a list of times that
    match the input variable bus_number"""
    bus_arrival_times = []
    for arrival_time in arrival_times:
        if arrival_time[0] == bus_number:
            time_ = epoch_to_date_string(arrival_time[1])
            bus_arrival_times.append(time_)
    return bus_arrival_times


def print_arrival_times(arrival_times):
    """Used for testing purposes"""
    for arrival_time in arrival_times:
        print arrival_time


def epoch_to_date_string(epoch_time):
    """Converts time since epoch in milliseconds to
    Hour:Minute:Second format"""
    return time.strftime("%H:%M:%S", time.localtime(epoch_time/1000))


def make_twilio_connection():
    """Establishes a connection to my Twilio account"""
    account_sid = "ACb9d4bd0e35f1####################"
    auth_token = "d75680887105####################"
    return TwilioRestClient(account_sid, auth_token)




