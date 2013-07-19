#include <fstream>
#include <sstream>
#include <vector>
#include <string>


int cpp_loadObjFile(const char* name, std::vector<float>& verticesNormalsAndTextures, std::vector<int>& faces)
{
	std::ifstream in(name);
	std::vector<float> vertices;
	std::vector<float> normals;
	std::vector<int> triangles;
	std::vector<int> faceNormals;

	while(in.good())
	{
		std::string line;
		std::getline(in, line);

		if(line.size())
		{
			//if(line[0] == '#')
			//	continue;

			std::istringstream sline(line);


			std::string head;
			std::getline(sline, head, ' ');

			if(head == "vn")
			{
			   float nx, ny, nz;
			   sline >> nx;
			   sline >> ny;
			   sline >> nz;
			   normals.push_back(nx);
			   normals.push_back(ny);
			   normals.push_back(nz);
			} else if(head == "v")
			{
			   float x, y, z;
			   sline >> x;
			   sline >> y;
			   sline >> z;
			   vertices.push_back(x);
			   vertices.push_back(y);
			   vertices.push_back(z);
			} else if(head == "f")
			{
			   int a, b, c;
			   int an, bn, cn;

			   char slash;
			   sline >> a;
			   sline >> slash;
			   sline >> slash;
			   sline >> an;

			   sline >> b;
			   sline >> slash;
			   sline >> slash;
			   sline >> bn;

			   sline >> c;
			   sline >> slash;
			   sline >> slash;
			   sline >> cn;

			  
			   triangles.push_back(a-1);
			   triangles.push_back(b-1);
			   triangles.push_back(c-1);
			   
			   faceNormals.push_back(an-1);
			   faceNormals.push_back(bn-1);
			   faceNormals.push_back(cn-1);
			}
		}
			
	}

	for(int fId = 0 ; fId < triangles.size()/3 ; fId++)
	{
		const int a = triangles[3*fId + 0];
		const int b = triangles[3*fId + 1];
		const int c = triangles[3*fId + 2];

		const int na = faceNormals[3*fId + 0];
		const int nb = faceNormals[3*fId + 1];
		const int nc = faceNormals[3*fId + 2];
		
		//add vertex A
		verticesNormalsAndTextures.push_back(vertices[3*a + 0]);	
		verticesNormalsAndTextures.push_back(vertices[3*a + 1]);	
		verticesNormalsAndTextures.push_back(vertices[3*a + 2]);

		verticesNormalsAndTextures.push_back(normals[3*na + 0]);	
		verticesNormalsAndTextures.push_back(normals[3*na + 1]);	
		verticesNormalsAndTextures.push_back(normals[3*na + 2]);
		
		verticesNormalsAndTextures.push_back(0.);
		verticesNormalsAndTextures.push_back(0.);

		//add vertex B
		verticesNormalsAndTextures.push_back(vertices[3*b + 0]);	
		verticesNormalsAndTextures.push_back(vertices[3*b + 1]);	
		verticesNormalsAndTextures.push_back(vertices[3*b + 2]);

		verticesNormalsAndTextures.push_back(normals[3*nb + 0]);	
		verticesNormalsAndTextures.push_back(normals[3*nb + 1]);	
		verticesNormalsAndTextures.push_back(normals[3*nb + 2]);
		
		verticesNormalsAndTextures.push_back(0.);
		verticesNormalsAndTextures.push_back(0.);
		
		//add vertex C
		verticesNormalsAndTextures.push_back(vertices[3*c + 0]);	
		verticesNormalsAndTextures.push_back(vertices[3*c + 1]);	
		verticesNormalsAndTextures.push_back(vertices[3*c + 2]);

		verticesNormalsAndTextures.push_back(normals[3*nc + 0]);	
		verticesNormalsAndTextures.push_back(normals[3*nc + 1]);	
		verticesNormalsAndTextures.push_back(normals[3*nc + 2]);
		
		verticesNormalsAndTextures.push_back(0.);
		verticesNormalsAndTextures.push_back(0.);

		faces.push_back(3*fId + 0);
		faces.push_back(3*fId + 1);
		faces.push_back(3*fId + 2);

	}
	return 0;
}
