import datetime

def currentTime( returnFormat=None ):
    # Description:
    #   Return the current computer time in the specified format
    #
    # inputs:
    #   returnFormat:   Flag for the format.
    #       options:    None (default, human readable string, 24hr clock)
    # outputs:
    #   return:         Computer time in chosen format

    if( returnFormat is None ):
        return str( datetime.datetime.now().time() )[:8]    # 8 to not return subseconds
    else:
        return currentTime( returnFormat=None )

#=========

def currentDate( returnFormat=None ):
    # Description:
    #   Return the current computer date in the specified format
    #
    # inputs:
    #   returnFormat:   Flag for the format.
    #       options:    None (default, human readable string, YYYY-MM-DD)

    if( returnFormat is None ):
        return str( datetime.datetime.now().date() )
    else:
        return currentDate( returnFormat=None )

#=========

def currentDateTime( returnFormat=None ):
    # Description:
    #   Return the current computer date and time in the specified format
    #
    # inputs:
    #   returnFormat:   Flag for the format
    #       options:    None (default, human readable string,)

    if( returnFormat is None ):
        return currentDate() + " " + currentTime()
    else:
        return currentDateTime( returnFormat=None )

#=========
