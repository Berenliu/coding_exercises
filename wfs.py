def wfs(g, u, states, active_points):
	state[u] = 1
	for p in g[u]:
		if state[p] == 0:
			active_points.append(p)
			state[p] = 1
			parents[p] = u
	while (len(active_points) > 0):
		u = active_poinst.pop(0)
		wfs(g, u, states, active_points)
	states[u] = 2
	return parents

def load_data()

if __name__ == "__main__":
	g, u = load_data()
	states = {}
	active_points = []
	parents = {}
	for p in g:
		states[p] = 0
		parents[p] = -1
	for p in g[u]:
		active_points.append(p)

	wfs(g, u, states, active_points, parents)