package test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.apache.commons.lang.StringEscapeUtils;

public class Test {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("lib.txt"));
		String line = "";
		Map<Integer, String> map= new HashMap<Integer, String>();
		try {
			int count = 0;
			while ((line = br.readLine()) != null) {
				line = StringEscapeUtils.unescapeJava(line);
				if(line.startsWith("{\"created_at\"")){
					count++;
					map.put(count, line);
				}else{
					map.put(count, map.get(count)+line);
				}
			}
			Set<Integer> keys = map.keySet();  //get all keys
			for(Integer i: keys)
			{
			    System.out.println(map.get(i));
			}
		} finally {
		    br.close();
		}
	}
}
