from collections import defaultdict

Step 1. Map:
 Domains --> Hits

dom_hits_map = [(x.split()[1], int(x.split()[0])) for x in cpdomains]
domains, hits = zip(*dom_hits_map)

Create defaultdict. There will be a list associated with each domain. Sum of that list is ACTUAL hits. This is relevant for the right answer.
dict_h = defaultdict(list)
for k in domains:
	dict_h[k].append()
	

Step 2: Map:

subdom_map = [(dom.split('.',i)[i], dom) for dom in domains for i in range(dom.count('.')+1)]

Step 3: Relate the two via a counter.

d = defaultdict(int)

for k, v in subdom_map:
	d[k] += dom_hits_map[v]

Step 4: Convert tuples in d back to their correct forms.

Convert defaultdict to a list. Create string where hits, subdomains are in correct order.

d_list = list(d.items())
to_print = [str(stuff[1]) + " " + stuff[0] for stuff in d_list]

VERY IMPORTANT: I debugged this. Dictionary overwrote one of the entries, because of unique k-v mapping.

Compared output to expected by the following:

list1 = output
list2 = expected

diff = [item for item in list1 if item not in list2]

Rewrite code to allow for multiple entries of the same domain.
