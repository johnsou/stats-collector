import os
import subprocess, re, json

def find_stats(raw_stats, stats_names):
	stats_by_line = raw_stats.split("\n")[-3]
	stats_names = [s.replace('%', '') for s in stats_names]
	stats = re.findall("\d+\.\d+", stats_by_line)
	filtered_stats = dict(zip(stats_names, stats))	
	
     	return filtered_stats	

def get_stats():

        memory_stats = subprocess.check_output(["sar" , "-r"]) 
        disku_stats  = subprocess.check_output(["sar" , "-b"])
	cpu_stats = subprocess.check_output(["sar", "-u"])
	disku = find_stats(disku_stats,["%tps", "%rtps", "%wtps"])
	memory = find_stats(memory_stats, ["%memused", "%commit"])
	cpu = find_stats(cpu_stats, ["%user", "%nice", "%system", "%iowait", "%steal", "%idle"])
	updates_stats = (subprocess.check_output(["/usr/lib/update-notifier/apt-check"],stderr=subprocess.STDOUT))
	updates = str(updates_stats).split(";")
        updates_names = ["available_updates", "available_security_updates"]
	updates = dict(zip(updates_names, updates))


	o = {"cpu": cpu , "memory": memory , "disku": disku, "updates": updates}

	return o

def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return [json.dumps(get_stats())]

