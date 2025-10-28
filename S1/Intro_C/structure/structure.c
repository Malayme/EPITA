struct coord
{
    int x;
    int y;
    int z;
};

int main(void)
{

    struct coord c;

    c.x = 10;
    c.y = 5;
    c.z = -2;

    struct coord *c_ptr = &c; 
    c_ptr->x = 15;
    c_ptr->y = -54;
    c_ptr->z = 42;

    int x = c.x;
    int y = c.y;
    int z = c.z;
}

int get_coord(const struct coord *coord)
{
    return coord->x;
}


