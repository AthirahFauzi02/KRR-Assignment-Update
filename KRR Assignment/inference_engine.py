class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = tuple(antecedent)
        self.consequent = tuple(consequent)
    
    def __eq__(self, other):
      return(
          isinstance(other, Rule) and
          self.antecedent == other.antecedent and
          self.consequent == other.consequent
      )

class InferenceEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, antecedent, consequent):
        rule = Rule(antecedent, consequent)
        self.rules.append(rule)

    def infer(self, facts):
        inferred_consequents = []
        for rule in self.rules:
            if all(fact in facts for fact in rule.antecedent) and all(fact in rule.antecedent for fact in facts):
                inferred_consequents.extend(rule.consequent)
        return inferred_consequents