


class CheckinAlreadyExists(Exception):
	"""
	Raise when user tries to do more then one checkin by specific habit
	"""
	
	
class WrongDateFormat(Exception):
	"""
	Raise when user send wrong date format
	Expected date format: 'yyyy-mm-dd'
	examples: '2026-03-05', '2026-12-01'
	"""