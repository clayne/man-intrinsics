class InstructionsDB(object):
    def __init__(self, instructions):
        grouped = {}
        architectures = set()
        for instr in instructions:
            list = grouped.get(instr.name, [])
            list.append(instr)
            grouped[instr.name] = list

            for architecture in instr.measurements.iterkeys():
                architectures.add(architecture)

        self.db = grouped
        self.architectures = architectures


    def find(self, instruction, cpuids):
        result = []
        for instr in self.db[instruction]:
            if instr.cpuid in cpuids:
                result.append(instr)

        return result
