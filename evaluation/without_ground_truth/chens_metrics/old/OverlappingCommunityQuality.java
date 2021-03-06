import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class OverlappingCommunityQuality {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String networkFile = args[0];									// Network File		
		String discoveredCommunityFile = args[1];					// Communities detected File
		boolean isUnweighted = false;									// Se rede é Weighted
		boolean isUndirected = false;									// Se rede é Directed
	
		for (String arg : args) {
			if (arg.equals("isUnweighted")) {
				isUnweighted = true;										// Se rede é Unweighted
			} 
			if (arg.equals("isUndirected")) {
				isUndirected = true;										// Se rede é Undirected
			}
		}
		
//		System.out.println("isUnweighted = " + isUnweighted + ", isUndirected = " + isUndirected);


		// Please look at the function definition for the value of
		// belongingVersion and belongingFunVersion
		int belongingVersion = 1;
		int belongingFunVersion = 1;

		
		double[] qualities = OverlappingCommunityQuality
				.computeOvQualityWithoutGroundTruth(networkFile, isUnweighted,
						isUndirected, discoveredCommunityFile,
						belongingVersion, belongingFunVersion);
		System.out.println("Q = " + qualities[0] + ", NQ = " + qualities[1]
				+ ", Qds = " + qualities[2] + ", intraEdges = " + qualities[3]
				+ ", intraDensity = " + qualities[4] + ", contraction = "
				+ qualities[5] + ", interEdges = " + qualities[6]
				+ ", expansion = " + qualities[7] + ", conductance = "
				+ qualities[8] + ", modularity degree = " + qualities[9]);
	}

	/**
	 * All the Overlapping community quality metrics (including local and
	 * global) without ground truth communities, with belonging coefficient and
	 * belonging function
	 * 
	 * @param networkFile
	 * @param isUnweighted
	 * @param isUndirected
	 * @param communityFile
	 * @param belongingVersion
	 *            0: fuzzy overlapping; 1: crisp overlapping with belonging
	 *            coefficients being 1/O_i; 2: crisp overlapping with belonging
	 *            coefficients being the strength of the node to the community.
	 * @param belongingFunVersion
	 *            0: average; 1: product; 2: max.
	 * @return
	 */
	public static double[] computeOvQualityWithoutGroundTruth(
			String networkFile, boolean isUnweighted, boolean isUndirected,
			String communityFile, int belongingVersion, int belongingFunVersion) {
		// long startTime = System.currentTimeMillis();

		// Get outgoing network
		HashMap<Integer, HashMap<Integer, Double>> outNet = new HashMap<Integer, HashMap<Integer, Double>>();
		// Return total weight. if undirected: 2m; if directed: m
		double[] weights = CommunityQuality.getNetwork(networkFile,
				isUnweighted, isUndirected, outNet);
		double totalWeight = weights[0];
		// double maxWeight = weights[1];
		// long numNodes = outNet.size();

		// If network is directed, get incoming network
		HashMap<Integer, HashMap<Integer, Double>> inNet = null;
		if (!isUndirected) {
			inNet = new HashMap<Integer, HashMap<Integer, Double>>();
			CommunityQuality.getReversedNetwork(networkFile, isUnweighted,
					isUndirected, inNet);
		}
		// System.out.println("Finish reading the network.");

		Map<Integer, Set<Integer>> mapCommunities = CommunityQuality
				.getMapCommunities(communityFile);
		int numComs = mapCommunities.size();
		// System.out.println("#com = " + numComs);

		HashMap<Integer, HashMap<Integer, Double>> ovNodeCommunities = OverlappingCommunityQuality
				.getCrispOverlappingNodeCommunities(communityFile);

		if (belongingVersion == 1) {
			// Crisp overlapping with belonging coefficients being 1/O_i
			OverlappingCommunityQuality
					.convertCrispToFuzzyOvCommunityWithNumComs(ovNodeCommunities);
		} else if (belongingVersion == 2) {
			// Crisp overlapping with belonging coefficients being the strength
			// of the node to the community
			OverlappingCommunityQuality
					.convertCrispToFuzzyOvCommunityWithNodeStrength(outNet,
							inNet, isUndirected, mapCommunities,
							ovNodeCommunities);
		}

		// Use type float to save memory
		double[] communitySizes = new double[numComs];
		double[][] communityWeights = new double[numComs][numComs];
		double[][] communityDensities = new double[numComs][numComs];

		// ///////////////////////////////////////////
		for (Map.Entry<Integer, HashMap<Integer, Double>> nodeItem : outNet.entrySet()) {		// Para vértices no grafo		
			int nodeId = nodeItem.getKey();																		// nodeId recebe id do vértices
			HashMap<Integer, Double> nodeNbs = nodeItem.getValue();										// Vizinhos do nó i
			HashMap<Integer, Double> nodeComs = ovNodeCommunities.get(nodeId);

			if (nodeNbs == null || nodeComs == null){															// Vértice que não foi adicionado a nenhuma comunidade 
//				System.out.println("ERRROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
//				System.out.println("Node ID = " + nodeId + " --- Node Nbs = " + nodeNbs + " --- Node Coms = " + nodeComs);
//				System.out.println(" ");
				;			// pass
			}

			else {	
				// Traverse the neighboring nodes of this node
				for (Map.Entry<Integer, Double> nbItem : nodeNbs.entrySet()) {
					
					if (nbItem.getKey() == null || nbItem.getValue() == null){
//						System.out.println("ERRROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
//						System.out.println("Nb ID = " + nbItem.getKey() + " --- weight = " + nbItem.getValue());
//						System.out.println(" ");
						;				
					}	
					
					else {	
						int nbId = nbItem.getKey();
						double weight = nbItem.getValue();
						if (ovNodeCommunities.get(nbId) == null){
//							System.out.println("ERRROR 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
//							System.out.println("ovNodeCommunities = " + ovNodeCommunities.get(nbId));
//							System.out.println(" ");
							;					
						}
						else {
							HashMap<Integer, Double> nbComs = ovNodeCommunities.get(nbId);	

//							System.out.println("Nb ID = " + nbId + " --- weight = " + weight + " --- Nb Coms = " + nbComs);			

							for (Map.Entry<Integer, Double> nodeComItem : nodeComs
									.entrySet()) {
								int nodeComId = nodeComItem.getKey();
								double nodeComFactor = nodeComItem.getValue();
								for (Map.Entry<Integer, Double> nbComItem : nbComs
										.entrySet()) {
									int nbComId = nbComItem.getKey();
									double nbComFactor = nbComItem.getValue();
			
									// Depends on belongingFunVersion
									if (belongingFunVersion == 0) {
										communityDensities[nodeComId][nbComId] += (nodeComFactor + nbComFactor) / 2;
										communityWeights[nodeComId][nbComId] += weight
												* (nodeComFactor + nbComFactor) / 2;
									} else if (belongingFunVersion == 1) {
										communityDensities[nodeComId][nbComId] += nodeComFactor
												* nbComFactor;
										communityWeights[nodeComId][nbComId] += weight
												* nodeComFactor * nbComFactor;
									} else if (belongingFunVersion == 2) {
										communityDensities[nodeComId][nbComId] += Math.max(
												nodeComFactor, nbComFactor);
										communityWeights[nodeComId][nbComId] += weight
												* Math.max(nodeComFactor, nbComFactor);
									}
								}	
							}
						}	
					}
				}
			} // node neighbors for
		} // nodes for
			// ///////////////////////////////////////

		for (int iComId = 0; iComId < numComs; ++iComId) {
			Set<Integer> iCommunity = mapCommunities.get(iComId);

			// Calculate community size with belonging factors
			for (int iNodeId : iCommunity) {
				communitySizes[iComId] += OverlappingCommunityQuality
						.getNodeBelongingFactor(ovNodeCommunities, iNodeId,
								iComId);
			}

			for (int jComId = 0; jComId < numComs; ++jComId) {

				// To save time, if there is no edge between the two
				// communities, we skip this pair
				if (communityWeights[iComId][jComId] == 0) {
					continue;
				}

				Set<Integer> jCommunity = mapCommunities.get(jComId);

				// Get the numerator and denominator of community density
				// double numerator = 0;
				double denominator = 0;
				for (int iNodeId : iCommunity) {
					// HashMap<Integer, Double> iNbs = outNet.get(iNodeId);
					double iFactor = OverlappingCommunityQuality
							.getNodeBelongingFactor(ovNodeCommunities, iNodeId,
									iComId);
					for (int jNodeId : jCommunity) {
						double jFactor = OverlappingCommunityQuality
								.getNodeBelongingFactor(ovNodeCommunities,
										jNodeId, jComId);
						if (iComId == jComId) {
							if (jNodeId != iNodeId) {
								if (belongingFunVersion == 0) {
									denominator += (iFactor + jFactor) / 2;
								} else if (belongingFunVersion == 1) {
									denominator += iFactor * jFactor;
								} else if (belongingFunVersion == 2) {
									denominator += Math.max(iFactor, jFactor);
								}
							}
						} else {
							if (belongingFunVersion == 0) {
								denominator += (iFactor + jFactor) / 2;
							} else if (belongingFunVersion == 1) {
								denominator += iFactor * jFactor;
							} else if (belongingFunVersion == 2) {
								denominator += Math.max(iFactor, jFactor);
							}
						}
					} // jNodeId for
				} // iNodeId for

				if (denominator == 0) {
					communityDensities[iComId][jComId] = 0;
				} else {
					communityDensities[iComId][jComId] = communityDensities[iComId][jComId]
							/ denominator;
				}
			} // j for
		} // i for

		// Compute average community quality of the sample
		double Q = 0;
		double NQ = 0;
		double Qds = 0;
		double intraEdges = 0;
		double intraDensity = 0;
		double contraction = 0;
		double interEdges = 0;
		// double interDensity = 0;
		double expansion = 0;
		double conductance = 0;

		// Average modularity degree metric
		double D = 0;

		for (int iComId = 0; iComId < numComs; ++iComId) {
			double iCommSize = communitySizes[iComId];
			double inWeights = communityWeights[iComId][iComId];
			double inDensity = communityDensities[iComId][iComId];
			// The number of outgoing edges from nodes inside the community to
			// the nodes ouside this community
			double outWeights = 0;
			// The number of incoming edges from nodes outside the community to
			// the nodes inside this community
			double out_incoming_weights = 0;
			double splitPenalty = 0;

			// The total weight of the subnetwork including the community and
			// its
			// neighboring communities
			double nebComTotalWeight = 0;
			HashSet<Integer> nebComs = new HashSet<Integer>();
			nebComs.add(iComId);

			for (int jComId = 0; jComId < numComs; ++jComId) {
				if (jComId != iComId) {
					double wij = communityWeights[iComId][jComId];
					double wji = communityWeights[jComId][iComId];
					outWeights += wij;
					if (wij != 0) {
						nebComs.add(jComId);
					}

					if (!isUndirected) {
						out_incoming_weights += wji;
						if (wji != 0) {
							nebComs.add(jComId);
						}
					}

					// double sp = (wij / totalWeight)
					// * communityDensities[iComId][jComId];
					double sp = wij * communityDensities[iComId][jComId];
					splitPenalty += sp;
				}
			}

			// Calculate nebComTotalWeight
			for (int icom : nebComs) {
				for (int jcom : nebComs) {
					nebComTotalWeight += communityWeights[icom][jcom];
				}
			}

			// System.out.println(inWeights + "\t" + outWeights + "\t"
			// + nebComTotalWeight + "\t" + nebNodeTotalWeight + "\t"
			// + wideNebNodeTotalWeight + "\t" + iCommSize + "\t"
			// + inDensity + "\t" + dc_out + "\t" + dc_out_denominator);

			if (isUndirected) {
				// modularity
				Q += inWeights / totalWeight
						- Math.pow((inWeights + outWeights) / totalWeight, 2);
				// Modularity Density Qds
				Qds += (inWeights / totalWeight)
						* inDensity
						- Math.pow(((inWeights + outWeights) / totalWeight)
								* inDensity, 2) - splitPenalty / totalWeight;

				if (nebComTotalWeight != 0) {
					NQ += inWeights
							/ nebComTotalWeight
							- Math.pow((inWeights + outWeights)
									/ nebComTotalWeight, 2);
				}
			} else {
				Q += inWeights
						/ totalWeight
						- ((inWeights + outWeights) * (inWeights + out_incoming_weights))
						/ Math.pow(totalWeight, 2);
				// Modularity Density Qds
				Qds += (inWeights / totalWeight)
						* inDensity
						- (((inWeights + outWeights) * (inWeights + out_incoming_weights)) / Math
								.pow(totalWeight, 2)) * Math.pow(inDensity, 2)
						- splitPenalty / totalWeight;

				if (nebComTotalWeight != 0) {
					NQ += inWeights
							/ nebComTotalWeight
							- ((inWeights + outWeights) * (inWeights + out_incoming_weights))
							/ Math.pow(nebComTotalWeight, 2);
				}
			}

			// intra-edges
			if (isUndirected) {
				intraEdges += inWeights / 2;
			} else {
				intraEdges += inWeights;
			}
			// contraction: average degree
			if (inWeights == 0 || iCommSize == 0) {
				contraction += 0;
			} else {
				contraction += inWeights / iCommSize;
			}
			// intra-density
			intraDensity += inDensity;
			interEdges += outWeights;
			// inter-density
			// if (numNodes == iCommSize) {
			// interDensity += 0;
			// } else {
			// interDensity += outWeights
			// / (iCommSize * (numNodes - iCommSize));
			// }
			if (outWeights == 0 || iCommSize == 0) {
				expansion += 0;
			} else {
				expansion += outWeights / iCommSize;
			}

			// Avoid that totalInterEdges==0 and communityEdges[i][i]==0
			if (outWeights == 0) {
				conductance += 0;
			} else {
				conductance += outWeights / (inWeights + outWeights);
			}

			// Average modularity degree metric
			if (iCommSize == 0) {
				D += 0;
			} else {
				D += (inWeights - outWeights) / iCommSize;
			}
		} // for

		// for local community detection algorithms
		double[] qualities = { Q, NQ, Qds, intraEdges / numComs,
				intraDensity / numComs, contraction / numComs,
				interEdges / numComs, expansion / numComs,
				conductance / numComs, D };

		// long endTime = System.currentTimeMillis();
		// System.out.println("running time: " + (endTime - startTime) + "ms");

		return qualities;
	}

	/**
	 * Compute entropy according to probability
	 * 
	 * @param p
	 * @return
	 */
	public static double logUtil(double p) {
		double value = 0;
		if (p > 0) {
			value = -p * (Math.log10(p) / Math.log10(2));
		}

		return value;
	}

	/**
	 * Return the belonging factor of a node to a community
	 * 
	 * @param ovNodeCommunities
	 * @param nodeId
	 * @param comId
	 * @return
	 */
	public static double getNodeBelongingFactor(
			HashMap<Integer, HashMap<Integer, Double>> ovNodeCommunities,
			int nodeId, int comId) {
		double factor = 0;
		HashMap<Integer, Double> communities = ovNodeCommunities.get(nodeId);
		if (communities.containsKey(comId)) {
			factor = communities.get(comId);
		}
		return factor;
	}

	/**
	 * 
	 * @param ovNodeCommunities
	 */
	public static void convertCrispToFuzzyOvCommunityWithNumComs(
			HashMap<Integer, HashMap<Integer, Double>> ovNodeCommunities) {
		for (Map.Entry<Integer, HashMap<Integer, Double>> nodeItem : ovNodeCommunities
				.entrySet()) {
			HashMap<Integer, Double> communities = nodeItem.getValue();
			double factor = 1.0 / communities.size();

			for (Map.Entry<Integer, Double> comItem : communities.entrySet()) {
				comItem.setValue(factor);
			}
		}
	}

	/**
	 * For undirected networks, only consider outgoing edges; for directed
	 * networks, consider both outgoing and incoming edges. Pay much attension
	 * to the overlapping situation.
	 * 
	 * @param outNet
	 * @param inNet
	 * @param isUndirected
	 * @param mapCommunities
	 * @param ovNodeCommunities
	 */
	public static void convertCrispToFuzzyOvCommunityWithNodeStrength(
			HashMap<Integer, HashMap<Integer, Double>> outNet,
			HashMap<Integer, HashMap<Integer, Double>> inNet,
			boolean isUndirected, Map<Integer, Set<Integer>> mapCommunities,
			HashMap<Integer, HashMap<Integer, Double>> ovNodeCommunities) {
		for (Map.Entry<Integer, HashMap<Integer, Double>> nodeItem : ovNodeCommunities
				.entrySet()) {
			int nodeId = nodeItem.getKey();
			HashMap<Integer, Double> communities = nodeItem.getValue();

			// Get the node strength
			HashMap<Integer, Double> outNodeNbs = outNet.get(nodeId);
			double totalNodeWeight = 0;
			for (Map.Entry<Integer, Double> nbItem : outNodeNbs.entrySet()) {
				int nbId = nbItem.getKey();
				double weight = nbItem.getValue();

				// Traverse each community this node belongs to to get the node
				// strength for this node to that community
				for (Map.Entry<Integer, Double> comItem : communities
						.entrySet()) {
					int comId = comItem.getKey();
					if (mapCommunities.get(comId).contains(nbId)) {
						comItem.setValue(comItem.getValue() + weight);
						totalNodeWeight += weight;
					}
				}
			}

			// if directed
			if (!isUndirected) {
				HashMap<Integer, Double> inNodeNbs = inNet.get(nodeId);
				for (Map.Entry<Integer, Double> nbItem : inNodeNbs.entrySet()) {
					int nbId = nbItem.getKey();
					double weight = nbItem.getValue();

					// Traverse each community this node belongs to to get the
					// node
					// strength for this node to that community
					for (Map.Entry<Integer, Double> comItem : communities
							.entrySet()) {
						int comId = comItem.getKey();
						if (mapCommunities.get(comId).contains(nbId)) {
							comItem.setValue(comItem.getValue() + weight);
							totalNodeWeight += weight;
						}
					}
				}
			}

			// divided by the total node weight
			for (Map.Entry<Integer, Double> comItem : communities.entrySet()) {
				// if (comItem.getValue() == 0 && totalNodeWeight == 0) {
				// System.out.println("NaN");
				// }

				if (comItem.getValue() == 0 || totalNodeWeight == 0) {
					comItem.setValue(0.0);
				} else {
					comItem.setValue(comItem.getValue() / totalNodeWeight);
				}
			}
		}
	}

	/**
	 * The id of communities start from 0
	 * 
	 * @param communityFile
	 * @return
	 */
	public static HashMap<Integer, HashMap<Integer, Double>> getCrispOverlappingNodeCommunities(
			String communityFile) {
		HashMap<Integer, HashMap<Integer, Double>> nodeCommunities = new HashMap<Integer, HashMap<Integer, Double>>();
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(
					new FileInputStream(communityFile)));
			String tmp = null;
			String[] nodes = null;
			// The id of communities start from 0
			int count = 0;

			while ((tmp = br.readLine()) != null) {
				tmp = tmp.trim();
				tmp = tmp.replaceAll("\\s+", " ");
				nodes = tmp.split(" ");

				for (int i = 0; i < nodes.length; ++i) {
					int node = Integer.parseInt(nodes[i]);

					if (!nodeCommunities.containsKey(node)) {
						nodeCommunities.put(node,
								new HashMap<Integer, Double>());
					}

					HashMap<Integer, Double> communities = nodeCommunities
							.get(node);
					communities.put(count, 0.0);
				}

				++count;
			}

			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		return nodeCommunities;
	}

	/**
	 * The id of communities start from 0
	 * 
	 * @param communityFile
	 * @return
	 */
	public static HashMap<Integer, HashSet<Integer>> getOverlappingNodeCommunities(
			String communityFile) {
		HashMap<Integer, HashSet<Integer>> nodeCommunities = new HashMap<Integer, HashSet<Integer>>();
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(
					new FileInputStream(communityFile)));
			String tmp = null;
			String[] nodes = null;
			// The id of communities start from 0
			int count = 0;

			while ((tmp = br.readLine()) != null) {
				tmp = tmp.trim();
				tmp = tmp.replaceAll("\\s+", " ");
				nodes = tmp.split(" ");

				for (int i = 0; i < nodes.length; ++i) {
					int node = Integer.parseInt(nodes[i]);

					if (!nodeCommunities.containsKey(node)) {
						nodeCommunities.put(node, new HashSet<Integer>());
					}

					HashSet<Integer> communities = nodeCommunities.get(node);
					communities.add(count);
				}

				++count;
			}

			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		return nodeCommunities;
	}

}
