def cron_hour_interval(interval_hour_str, start_hour_str):
    """
    Ingests a starting hour and an interval in hours and outputs a list of hours
    separated by comma for use in a cron job
    """

    allowed_intervals = [1, 2, 3, 4, 6, 8, 12, 24]
    all_hours_list = [num for num in range(0, 25)]
    cron_hours_list = []
    separator = ","

    interval_hour = int(interval_hour_str)
    start_hour = int(start_hour_str)

    if interval_hour not in allowed_intervals:
        raise ValueError(
            "Interval must be a whole number factor of 24, i.e. 1, 2, 3, 4, 6, 8, etc"
        )

    if start_hour not in all_hours_list:
        raise ValueError("Start hour must be a whole number between 0 and 23")

    unfiltered_cron_hours_list = range(
        (start_hour - 24), (start_hour + 24), interval_hour
    )

    cron_hours_list = set(unfiltered_cron_hours_list) & set(all_hours_list)
    cron_hours_str = separator.join(map(str, cron_hours_list))

    return cron_hours_str


class FilterModule(object):
    """
    custom jinja2 filter
    """

    def filters(self):
        return {"cron_hour_interval": cron_hour_interval}
