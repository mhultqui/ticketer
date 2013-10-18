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
	n = 1
	last = a1
	while n < num:
		last = t.next_Ticket(last)
		n = n+1
	return last

def ticketCheck2(a1, num):
	n = 0
	num = num - 1
	subnum = num % 31337

	last = a1
	while n < subnum:
		last = t.next_Ticket(last)
		n = n+1
	return last

index = 31300
while index < 31350:
	print index, ticketCheck(4829, index)
	print index, ticketCheck2(4829, index)
	index+=1

#print 0, ticketCheck( 4829, 1)
#print 0, ticketCheck2(4829, 1)

#print 1, ticketCheck( 4829, 31336)
#print 1, ticketCheck2(4829, 31336)
#print 2, ticketCheck( 4829, 31338)
#print 2, ticketCheck2(4829, 31338)

#temp1 = ticketCheck (10802, 1858540)
#print 3, temp1
#temp2 = ticketCheck2(10802, 1858540)
#print 3, temp2
