#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, e;
    cin >> n >> e;

    vector<vector<int>> d;
    for (int i = 0; i < e; i++) {
        int e1, e2, l;
        cin >> e1 >> e2 >> l;
        d.push_back({e1, e2, l});
    }

    vector<int> dist(n, 30000);
    dist[0] = 0;

    for (int i = 0; i <= n; i++) {
        for (auto edge : d) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            
            if (dist[u - 1] != 30000 && dist[u - 1] + w < dist[v - 1]) {
                dist[v - 1] = dist[u - 1] + w;
            }
        }
    }

    for (int i = 0; i < dist.size(); i++) {
        cout << dist[i] << " ";
    }

    return 0;
}
