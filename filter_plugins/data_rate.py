def data_rate_to_hex(allowed_rate_list):
    """
    Convert a list of allowed data rates to a hex value that can be understood
    by a radio driver
    """

    # Set some variables here, the bit mapping table is required to map the data
    # rate bit position to corresponding integer values
    all_data_rates = [1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54]
    bit_table = [1, 2, 5.5, 11, 6, 9, 12, 18, 24, 36, 48, 54]
    running_total = 0

    # Perform data validation on the allowed_rate_list passed to the function
    # against the all_data_rates set
    for rate in allowed_rate_list:
        if rate not in all_data_rates:
            raise ValueError("Invalid data rates passed to filter")

    # Convert the allowed rates to bit values by raising two to the power of the
    # value and get the sum total
    for i, val in enumerate(allowed_rate_list):
        running_total += 2 ** (bit_table.index(val))

    # Convert sum total to hex and return
    allowed_rates_hex_value = "{0:00(1)x})".format(running_total, 6)
    return allowed_rates_hex_value


class FilterModule(object):
    """
    custom jinja2 filter
    """

    def filters(self):
        return {"allowed_rates_hex_value": allowed_rates_hex_value}
