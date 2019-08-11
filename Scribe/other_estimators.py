##############################################################################
# Run pairwise Correlation over the data
def corr(self, number_of_processes=1):

    self.corr_results = pandas.DataFrame({node_id: [np.nan for i in self.node_ids] for node_id in self.node_ids}, index=self.node_ids)
    if number_of_processes > 1: temp_input = []

    for id1 in self.node_ids:
        for id2 in self.node_ids:

            if id1 == id2: continue

            if number_of_processes == 1:
                self.corr_results.loc[id1, id2] = __individual_corr((id1, id2, self.expression_concatenated.loc[id1], self.expression_concatenated.loc[id2]))[2]
            else:
                temp_input.append((id1, id2, self.expression_concatenated.loc[id1], self.expression_concatenated.loc[id2]))

    if number_of_processes > 1:
        tmp_results = Pool(number_of_processes).map(__individual_corr, temp_input)
        for t in tmp_results: self.corr_results.loc[t[0], t[1]] = t[2]

    return self.corr_results


##############################################################################
# Run pairwise MI over the data
def mi(self, number_of_processes=1):

    self.mi_results = pandas.DataFrame({node_id: [np.nan for i in self.node_ids] for node_id in self.node_ids}, index=self.node_ids)
    if number_of_processes > 1: temp_input = []

    for id1 in self.node_ids:
        for id2 in self.node_ids:

            if id1 == id2: continue

            if number_of_processes == 1:
                self.mi_results.loc[id1, id2] = __individual_mi((id1, id2,[[i] for i in self.expression_concatenated.loc[id1]],[[j] for j in self.expression_concatenated.loc[id2]] ))[2]
            else:
                temp_input.append((id1, id2,[[i] for i in self.expression_concatenated.loc[id1]],[[j] for j in self.expression_concatenated.loc[id2]] ))

    if number_of_processes > 1:
        tmp_results = Pool(number_of_processes).map(__individual_mi, temp_input)
        for t in tmp_results: self.mi_results.loc[t[0], t[1]] = t[2]

    return self.mi_results