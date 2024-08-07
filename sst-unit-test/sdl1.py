# Automatically generated by SST
import sst

# Define SST Program Options:
sst.setProgramOption("timebase", "1ps")
sst.setProgramOption("stopAtCycle", "0 ns")

# Define the SST Components:
comp_gpu0 = sst.Component("gpu0", "macsimComponent.macsimComponent")
comp_gpu0.addParams({
     "trace_file" : "trace_file_list",
     "mem_size" : "4*1024*1024*1024",
     "command_line" : "--use_memhierarchy=1",
     "debug_level" : "8",
     "num_link" : "16",
     "frequency" : "4 Ghz",
     "output_dir" : "results",
     "debug" : "0",
     "param_file" : "params.in"
})
comp_core0l1icache = sst.Component("core0l1icache", "memHierarchy.Cache")
comp_core0l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core0l1dcache = sst.Component("core0l1dcache", "memHierarchy.Cache")
comp_core0l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core1l1icache = sst.Component("core1l1icache", "memHierarchy.Cache")
comp_core1l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core1l1dcache = sst.Component("core1l1dcache", "memHierarchy.Cache")
comp_core1l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core2l1icache = sst.Component("core2l1icache", "memHierarchy.Cache")
comp_core2l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core2l1dcache = sst.Component("core2l1dcache", "memHierarchy.Cache")
comp_core2l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core3l1icache = sst.Component("core3l1icache", "memHierarchy.Cache")
comp_core3l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core3l1dcache = sst.Component("core3l1dcache", "memHierarchy.Cache")
comp_core3l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core4l1icache = sst.Component("core4l1icache", "memHierarchy.Cache")
comp_core4l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core4l1dcache = sst.Component("core4l1dcache", "memHierarchy.Cache")
comp_core4l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core5l1icache = sst.Component("core5l1icache", "memHierarchy.Cache")
comp_core5l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core5l1dcache = sst.Component("core5l1dcache", "memHierarchy.Cache")
comp_core5l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core6l1icache = sst.Component("core6l1icache", "memHierarchy.Cache")
comp_core6l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core6l1dcache = sst.Component("core6l1dcache", "memHierarchy.Cache")
comp_core6l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core7l1icache = sst.Component("core7l1icache", "memHierarchy.Cache")
comp_core7l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core7l1dcache = sst.Component("core7l1dcache", "memHierarchy.Cache")
comp_core7l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core8l1icache = sst.Component("core8l1icache", "memHierarchy.Cache")
comp_core8l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core8l1dcache = sst.Component("core8l1dcache", "memHierarchy.Cache")
comp_core8l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core9l1icache = sst.Component("core9l1icache", "memHierarchy.Cache")
comp_core9l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core9l1dcache = sst.Component("core9l1dcache", "memHierarchy.Cache")
comp_core9l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core10l1icache = sst.Component("core10l1icache", "memHierarchy.Cache")
comp_core10l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core10l1dcache = sst.Component("core10l1dcache", "memHierarchy.Cache")
comp_core10l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core11l1icache = sst.Component("core11l1icache", "memHierarchy.Cache")
comp_core11l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core11l1dcache = sst.Component("core11l1dcache", "memHierarchy.Cache")
comp_core11l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core12l1icache = sst.Component("core12l1icache", "memHierarchy.Cache")
comp_core12l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core12l1dcache = sst.Component("core12l1dcache", "memHierarchy.Cache")
comp_core12l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core13l1icache = sst.Component("core13l1icache", "memHierarchy.Cache")
comp_core13l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core13l1dcache = sst.Component("core13l1dcache", "memHierarchy.Cache")
comp_core13l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core14l1icache = sst.Component("core14l1icache", "memHierarchy.Cache")
comp_core14l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core14l1dcache = sst.Component("core14l1dcache", "memHierarchy.Cache")
comp_core14l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core15l1icache = sst.Component("core15l1icache", "memHierarchy.Cache")
comp_core15l1icache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "1",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "0",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_core15l1dcache = sst.Component("core15l1dcache", "memHierarchy.Cache")
comp_core15l1dcache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "3",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "1",
     "cache_size" : "64 KB",
     "mshr_latency_cycles" : "0"
})
comp_gpu0l1l2bus = sst.Component("gpu0l1l2bus", "memHierarchy.Bus")
comp_gpu0l1l2bus.addParams({
     "debug" : "0",
     "bus_frequency" : "4 Ghz"
})
comp_gpu0l2cache = sst.Component("gpu0l2cache", "memHierarchy.Cache")
comp_gpu0l2cache.addParams({
     "debug_level" : "8",
     "debug" : "0",
     "access_latency_cycles" : "8",
     "cache_frequency" : "4 Ghz",
     "replacement_policy" : "lru",
     "coherence_protocol" : "MESI",
     "associativity" : "8",
     "cache_line_size" : "128",
     "directory_at_next_level" : "0",
     "statistics" : "1",
     "L1" : "0",
     "cache_size" : "512 KB",
     "mshr_latency_cycles" : "0"
})
comp_memory0 = sst.Component("memory0", "memHierarchy.MemController")
comp_memory0.addParams({
     "debug" : "0",
     "coherence_protocol" : "MESI",
     "statistics" : "1",
     "backend.mem_size" : "4096",
     "clock" : "1 GHz",
     "access_time" : "97 ns",
     "rangeStart" : "0"
})


# Define the SST Component Statistics Information
# Define SST Statistics Options:

# Define Component Statistics Information:


# Define SST Simulation Link Information
link_c0_icache = sst.Link("link_c0_icachec0_icache")
link_c0_icache.connect( (comp_gpu0, "core0-icache", "1000ps"), (comp_core0l1icache, "high_network_0", "1000ps") )
link_c0_dcache = sst.Link("link_c0_dcachec0_dcache")
link_c0_dcache.connect( (comp_gpu0, "core0-dcache", "1000ps"), (comp_core0l1dcache, "high_network_0", "1000ps") )
link_c1_icache = sst.Link("link_c1_icachec1_icache")
link_c1_icache.connect( (comp_gpu0, "core1-icache", "1000ps"), (comp_core1l1icache, "high_network_0", "1000ps") )
link_c1_dcache = sst.Link("link_c1_dcachec1_dcache")
link_c1_dcache.connect( (comp_gpu0, "core1-dcache", "1000ps"), (comp_core1l1dcache, "high_network_0", "1000ps") )
link_c2_icache = sst.Link("link_c2_icachec2_icache")
link_c2_icache.connect( (comp_gpu0, "core2-icache", "1000ps"), (comp_core2l1icache, "high_network_0", "1000ps") )
link_c2_dcache = sst.Link("link_c2_dcachec2_dcache")
link_c2_dcache.connect( (comp_gpu0, "core2-dcache", "1000ps"), (comp_core2l1dcache, "high_network_0", "1000ps") )
link_c3_icache = sst.Link("link_c3_icachec3_icache")
link_c3_icache.connect( (comp_gpu0, "core3-icache", "1000ps"), (comp_core3l1icache, "high_network_0", "1000ps") )
link_c3_dcache = sst.Link("link_c3_dcachec3_dcache")
link_c3_dcache.connect( (comp_gpu0, "core3-dcache", "1000ps"), (comp_core3l1dcache, "high_network_0", "1000ps") )
link_c4_icache = sst.Link("link_c4_icachec4_icache")
link_c4_icache.connect( (comp_gpu0, "core4-icache", "1000ps"), (comp_core4l1icache, "high_network_0", "1000ps") )
link_c4_dcache = sst.Link("link_c4_dcachec4_dcache")
link_c4_dcache.connect( (comp_gpu0, "core4-dcache", "1000ps"), (comp_core4l1dcache, "high_network_0", "1000ps") )
link_c5_icache = sst.Link("link_c5_icachec5_icache")
link_c5_icache.connect( (comp_gpu0, "core5-icache", "1000ps"), (comp_core5l1icache, "high_network_0", "1000ps") )
link_c5_dcache = sst.Link("link_c5_dcachec5_dcache")
link_c5_dcache.connect( (comp_gpu0, "core5-dcache", "1000ps"), (comp_core5l1dcache, "high_network_0", "1000ps") )
link_c6_icache = sst.Link("link_c6_icachec6_icache")
link_c6_icache.connect( (comp_gpu0, "core6-icache", "1000ps"), (comp_core6l1icache, "high_network_0", "1000ps") )
link_c6_dcache = sst.Link("link_c6_dcachec6_dcache")
link_c6_dcache.connect( (comp_gpu0, "core6-dcache", "1000ps"), (comp_core6l1dcache, "high_network_0", "1000ps") )
link_c7_icache = sst.Link("link_c7_icachec7_icache")
link_c7_icache.connect( (comp_gpu0, "core7-icache", "1000ps"), (comp_core7l1icache, "high_network_0", "1000ps") )
link_c7_dcache = sst.Link("link_c7_dcachec7_dcache")
link_c7_dcache.connect( (comp_gpu0, "core7-dcache", "1000ps"), (comp_core7l1dcache, "high_network_0", "1000ps") )
link_c8_icache = sst.Link("link_c8_icachec8_icache")
link_c8_icache.connect( (comp_gpu0, "core8-icache", "1000ps"), (comp_core8l1icache, "high_network_0", "1000ps") )
link_c8_dcache = sst.Link("link_c8_dcachec8_dcache")
link_c8_dcache.connect( (comp_gpu0, "core8-dcache", "1000ps"), (comp_core8l1dcache, "high_network_0", "1000ps") )
link_c9_icache = sst.Link("link_c9_icachec9_icache")
link_c9_icache.connect( (comp_gpu0, "core9-icache", "1000ps"), (comp_core9l1icache, "high_network_0", "1000ps") )
link_c9_dcache = sst.Link("link_c9_dcachec9_dcache")
link_c9_dcache.connect( (comp_gpu0, "core9-dcache", "1000ps"), (comp_core9l1dcache, "high_network_0", "1000ps") )
link_c10_icache = sst.Link("link_c10_icachec10_icache")
link_c10_icache.connect( (comp_gpu0, "core10-icache", "1000ps"), (comp_core10l1icache, "high_network_0", "1000ps") )
link_c10_dcache = sst.Link("link_c10_dcachec10_dcache")
link_c10_dcache.connect( (comp_gpu0, "core10-dcache", "1000ps"), (comp_core10l1dcache, "high_network_0", "1000ps") )
link_c11_icache = sst.Link("link_c11_icachec11_icache")
link_c11_icache.connect( (comp_gpu0, "core11-icache", "1000ps"), (comp_core11l1icache, "high_network_0", "1000ps") )
link_c11_dcache = sst.Link("link_c11_dcachec11_dcache")
link_c11_dcache.connect( (comp_gpu0, "core11-dcache", "1000ps"), (comp_core11l1dcache, "high_network_0", "1000ps") )
link_c12_icache = sst.Link("link_c12_icachec12_icache")
link_c12_icache.connect( (comp_gpu0, "core12-icache", "1000ps"), (comp_core12l1icache, "high_network_0", "1000ps") )
link_c12_dcache = sst.Link("link_c12_dcachec12_dcache")
link_c12_dcache.connect( (comp_gpu0, "core12-dcache", "1000ps"), (comp_core12l1dcache, "high_network_0", "1000ps") )
link_c13_icache = sst.Link("link_c13_icachec13_icache")
link_c13_icache.connect( (comp_gpu0, "core13-icache", "1000ps"), (comp_core13l1icache, "high_network_0", "1000ps") )
link_c13_dcache = sst.Link("link_c13_dcachec13_dcache")
link_c13_dcache.connect( (comp_gpu0, "core13-dcache", "1000ps"), (comp_core13l1dcache, "high_network_0", "1000ps") )
link_c14_icache = sst.Link("link_c14_icachec14_icache")
link_c14_icache.connect( (comp_gpu0, "core14-icache", "1000ps"), (comp_core14l1icache, "high_network_0", "1000ps") )
link_c14_dcache = sst.Link("link_c14_dcachec14_dcache")
link_c14_dcache.connect( (comp_gpu0, "core14-dcache", "1000ps"), (comp_core14l1dcache, "high_network_0", "1000ps") )
link_c15_icache = sst.Link("link_c15_icachec15_icache")
link_c15_icache.connect( (comp_gpu0, "core15-icache", "1000ps"), (comp_core15l1icache, "high_network_0", "1000ps") )
link_c15_dcache = sst.Link("link_c15_dcachec15_dcache")
link_c15_dcache.connect( (comp_gpu0, "core15-dcache", "1000ps"), (comp_core15l1dcache, "high_network_0", "1000ps") )
link_c0_icache_bus = sst.Link("link_c0_icache_busc0_icache_bus")
link_c0_icache_bus.connect( (comp_core0l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_0", "10000ps") )
link_c0_dcache_bus = sst.Link("link_c0_dcache_busc0_dcache_bus")
link_c0_dcache_bus.connect( (comp_core0l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_1", "10000ps") )
link_c1_icache_bus = sst.Link("link_c1_icache_busc1_icache_bus")
link_c1_icache_bus.connect( (comp_core1l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_2", "10000ps") )
link_c1_dcache_bus = sst.Link("link_c1_dcache_busc1_dcache_bus")
link_c1_dcache_bus.connect( (comp_core1l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_3", "10000ps") )
link_c2_icache_bus = sst.Link("link_c2_icache_busc2_icache_bus")
link_c2_icache_bus.connect( (comp_core2l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_4", "10000ps") )
link_c2_dcache_bus = sst.Link("link_c2_dcache_busc2_dcache_bus")
link_c2_dcache_bus.connect( (comp_core2l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_5", "10000ps") )
link_c3_icache_bus = sst.Link("link_c3_icache_busc3_icache_bus")
link_c3_icache_bus.connect( (comp_core3l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_6", "10000ps") )
link_c3_dcache_bus = sst.Link("link_c3_dcache_busc3_dcache_bus")
link_c3_dcache_bus.connect( (comp_core3l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_7", "10000ps") )
link_c4_icache_bus = sst.Link("link_c4_icache_busc4_icache_bus")
link_c4_icache_bus.connect( (comp_core4l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_8", "10000ps") )
link_c4_dcache_bus = sst.Link("link_c4_dcache_busc4_dcache_bus")
link_c4_dcache_bus.connect( (comp_core4l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_9", "10000ps") )
link_c5_icache_bus = sst.Link("link_c5_icache_busc5_icache_bus")
link_c5_icache_bus.connect( (comp_core5l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_10", "10000ps") )
link_c5_dcache_bus = sst.Link("link_c5_dcache_busc5_dcache_bus")
link_c5_dcache_bus.connect( (comp_core5l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_11", "10000ps") )
link_c6_icache_bus = sst.Link("link_c6_icache_busc6_icache_bus")
link_c6_icache_bus.connect( (comp_core6l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_12", "10000ps") )
link_c6_dcache_bus = sst.Link("link_c6_dcache_busc6_dcache_bus")
link_c6_dcache_bus.connect( (comp_core6l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_13", "10000ps") )
link_c7_icache_bus = sst.Link("link_c7_icache_busc7_icache_bus")
link_c7_icache_bus.connect( (comp_core7l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_14", "10000ps") )
link_c7_dcache_bus = sst.Link("link_c7_dcache_busc7_dcache_bus")
link_c7_dcache_bus.connect( (comp_core7l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_15", "10000ps") )
link_c8_icache_bus = sst.Link("link_c8_icache_busc8_icache_bus")
link_c8_icache_bus.connect( (comp_core8l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_16", "10000ps") )
link_c8_dcache_bus = sst.Link("link_c8_dcache_busc8_dcache_bus")
link_c8_dcache_bus.connect( (comp_core8l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_17", "10000ps") )
link_c9_icache_bus = sst.Link("link_c9_icache_busc9_icache_bus")
link_c9_icache_bus.connect( (comp_core9l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_18", "10000ps") )
link_c9_dcache_bus = sst.Link("link_c9_dcache_busc9_dcache_bus")
link_c9_dcache_bus.connect( (comp_core9l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_19", "10000ps") )
link_c10_icache_bus = sst.Link("link_c10_icache_busc10_icache_bus")
link_c10_icache_bus.connect( (comp_core10l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_20", "10000ps") )
link_c10_dcache_bus = sst.Link("link_c10_dcache_busc10_dcache_bus")
link_c10_dcache_bus.connect( (comp_core10l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_21", "10000ps") )
link_c11_icache_bus = sst.Link("link_c11_icache_busc11_icache_bus")
link_c11_icache_bus.connect( (comp_core11l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_22", "10000ps") )
link_c11_dcache_bus = sst.Link("link_c11_dcache_busc11_dcache_bus")
link_c11_dcache_bus.connect( (comp_core11l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_23", "10000ps") )
link_c12_icache_bus = sst.Link("link_c12_icache_busc12_icache_bus")
link_c12_icache_bus.connect( (comp_core12l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_24", "10000ps") )
link_c12_dcache_bus = sst.Link("link_c12_dcache_busc12_dcache_bus")
link_c12_dcache_bus.connect( (comp_core12l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_25", "10000ps") )
link_c13_icache_bus = sst.Link("link_c13_icache_busc13_icache_bus")
link_c13_icache_bus.connect( (comp_core13l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_26", "10000ps") )
link_c13_dcache_bus = sst.Link("link_c13_dcache_busc13_dcache_bus")
link_c13_dcache_bus.connect( (comp_core13l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_27", "10000ps") )
link_c14_icache_bus = sst.Link("link_c14_icache_busc14_icache_bus")
link_c14_icache_bus.connect( (comp_core14l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_28", "10000ps") )
link_c14_dcache_bus = sst.Link("link_c14_dcache_busc14_dcache_bus")
link_c14_dcache_bus.connect( (comp_core14l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_29", "10000ps") )
link_c15_icache_bus = sst.Link("link_c15_icache_busc15_icache_bus")
link_c15_icache_bus.connect( (comp_core15l1icache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_30", "10000ps") )
link_c15_dcache_bus = sst.Link("link_c15_dcache_busc15_dcache_bus")
link_c15_dcache_bus.connect( (comp_core15l1dcache, "low_network_0", "10000ps"), (comp_gpu0l1l2bus, "high_network_31", "10000ps") )
link_bus_gpu0l2cache = sst.Link("link_bus_gpu0l2cachebus_gpu0l2cache")
link_bus_gpu0l2cache.connect( (comp_gpu0l1l2bus, "low_network_0", "10000ps"), (comp_gpu0l2cache, "high_network_0", "10000ps") )
link_gpu0l2_mem0 = sst.Link("link_gpu0l2_mem0gpu0l2_mem0")
link_gpu0l2_mem0.connect( (comp_gpu0l2cache, "low_network_0", "10000ps"), (comp_memory0, "direct_link", "10000ps") )
# End of generated output.

