from collections import defaultdict, deque

class Graph():
	def __init__(self):
		self.d = defaultdict(list)	
	#############
	def add_edge(self, n1, n2):
		self.d[n1].append(n2)
		self.d[n2].append(n1)
	def bfspath(self, start, end):
		q = deque([(start,)])
		visited = dict.fromkeys(self.d.keys())
		parent = dict.fromkeys(self.d.keys())
		path = []
		while q:
			nextnode = q.popleft()[0]
			nbrs = self.d[nextnode]
			for n in nbrs:
				if not visited[n]:
					visited[n] = True
					q.extend([(n,)])
					parent[n] = nextnode
					if n == end:
						path = [n]
						p = parent[n]
						while p!=start:
							path.append(p)
							p = parent[p]
						return path
		return []
	########################################
def prev_char(c):
	if c=='a':
		return 'z'
	else:
		return chr(ord(c) - 1)

def next_char(c):
	if c=='z':
		return 'a'
	else:
		return chr(ord(c) + 1)


def _make_cands2(w):
	n = []
	for i in range(len(w)):
		wsn, wsp = list(w), list(w)
		wsn[i] = next_char(wsn[i])
		wsp[i] = prev_char(wsp[i])
		n.extend([''.join(wsn), ''.join(wsp)])
	return n

class SmartWordToy():
	def __init__(self):
		self.G = Graph()
		
	def is_forbidden(self, w):
		if self.fsets:
			for s in self.fsets:
				if (w[0] in s[0]) and (w[1] in s[1]) and (w[2] in s[2]) and (w[3] in s[3]):
					return True
		else:
			return False
		return False
		
	def create_forbiddensets(self, forbid):
		fsets = []
		for pattern in forbid:
			fp = pattern.split(' ')
			# a1 in set1 and a2 in set2 .. 
			fsets.append([set(ip) for ip in fp])
		self.fsets = fsets
	#####################################################
	def minPresses(self, start, finish, forbid):
		self.create_forbiddensets(forbid)
		G = self.G
		G.d[start] = []
		def discover_nbrs(n):
			nbrs = _make_cands2(n)
			finished = False
			new_nbrs = []
			for nb in nbrs:
				if not self.is_forbidden(nb)\
					and nb not in G.d:
						#G.add_node(nb)
						G.add_edge(nb, n)
						new_nbrs.append(nb)
						if nb == finish:
							finished = True
							break
			return new_nbrs, finished
		dq = deque([(start,)])
		while dq:
			nextnode = dq.popleft()[0]
			nbrs, finished = discover_nbrs(nextnode)
			dq.extend([(nx,) for nx in nbrs])
			if finished:
				path = G.bfspath(start, finish)
				return len(path)
		if not finished:
			return -1

if __name__ == '__main__':
	i1 = "aaaa", "zzzz", ("a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a")
	i2 = "aaaa", "bbbb", ('')
	i3 = "aaaa", "mmnn", ('')
	i4 = "aaaa", "zzzz", ("bz a a a", "a bz a a", "a a bz a", "a a a bz")
	i5 = "aaaa", "bbbb", ("b b b b",)
	i6 = "aaaa", "zzzz", ("cdefghijklmnopqrstuvwxyz a a a", "a cdefghijklmnopqrstuvwxyz a a", "a a cdefghijklmnopqrstuvwxyz a", "a a a cdefghijklmnopqrstuvwxyz")
	i7 = "zzzz", "aaaa",\
	("abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
	"abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk")
	i8 = "aaaa", "xxxx", ("xz xz xz z", "xa xa xa b")
	import time
	ts = time.time()
	for j, i in enumerate([i1, i2, i3, i4, i5, i6, i7, i8][:]):
		SW = SmartWordToy()
		print "Test %d : %d" % (j+1, SW.minPresses(i[0], i[1], i[2]))
	print time.time() -ts, 'seconds'