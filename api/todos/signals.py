from django.dispatch import Signal

# Define a custom signal
post_request_signal = Signal()

# Connect a signal handler to the custom signal
def my_function(sender, request, **kwargs):
    # Your logic here
    print("POST request received")

post_request_signal.connect(my_function)