#! /usr/bin/python

class Dict(dict):
	def __missing__(self, key):
		tempvar = (key*31334) % 31337
		self[key] = tempvar
		return tempvar

class TicketChecker:
	ticket_list = Dict()
	def next_Ticket(self, a):
		return self.ticket_list[a];

t = TicketChecker()
def ticketCheck(a1, num):
	subnum = num % 31337
	n = 1
	last = a1
	while n < subnum:
		last = t.next_Ticket(last)
		n = n + 1
	return last


print 1, ticketCheck(16231, 8)
print 2, ticketCheck(6086, 18)
print 5, ticketCheck(10802, 1858540)
