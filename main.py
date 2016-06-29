import TriMetAlert as t


if __name__ == "__main__":
    response = t.get_trimet_response()
    arrivals = t.get_arrivals(response)
    times = t.get_arrival_times(arrivals)
    my_bus_times = t.get_bus_arrival_times(times, 19)

    my_twilio_number = "+160########"
    my_cell_number = "+160########"
    con_obj = t.make_twilio_connection()
    con_obj.messages.create(body='\n'.join(my_bus_times), from_=my_twilio_number, to=my_cell_number)
